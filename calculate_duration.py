#!/usr/bin/env python3
"""
Calculate duration between git commits for course sections.
Usage: python calculate_duration.py [section_name]
Example: python calculate_duration.py section01
"""

import subprocess
import sys
from datetime import datetime


def get_commit_timestamps(section_filter=None):
    """Get commit timestamps from git log."""
    cmd = ["git", "log", "--format=%ad|%s", "--date=iso", "--all"]
    result = subprocess.run(cmd, capture_output=True, text=True)

    commits = []
    for line in result.stdout.strip().split("\n"):
        if "|" not in line:
            continue
        timestamp, message = line.split("|", 1)
        if section_filter and section_filter not in message.lower():
            continue
        commits.append(
            {
                "timestamp": datetime.fromisoformat(timestamp.rsplit(" ", 1)[0]),
                "message": message,
            }
        )

    return commits


def calculate_section_duration(section_name):
    """Calculate duration for a specific section."""
    commits = get_commit_timestamps(section_name)

    if len(commits) < 2:
        print(f"Not enough commits found for {section_name}")
        return

    # Find begin and complete commits
    begin_commit = None
    complete_commit = None

    for commit in reversed(commits):  # Reverse to get chronological order
        if "begin" in commit["message"].lower():
            begin_commit = commit
        elif "complete" in commit["message"].lower():
            complete_commit = commit

    if begin_commit and complete_commit:
        duration = complete_commit["timestamp"] - begin_commit["timestamp"]
        hours = duration.total_seconds() / 3600
        minutes = duration.total_seconds() / 60

        print(f"\n{section_name.upper()}")
        print(f"Started: {begin_commit['timestamp'].strftime('%Y.%m.%d %I:%M%p')}")
        print(f"Completed: {complete_commit['timestamp'].strftime('%Y.%m.%d %I:%M%p')}")

        if hours >= 1:
            print(f"Duration: ~{hours:.1f} hours")
        else:
            print(f"Duration: ~{int(minutes)} minutes")
    else:
        print(f"Could not find both begin and complete commits for {section_name}")


def list_all_sections():
    """List all sections with timestamps."""
    commits = get_commit_timestamps()

    print("\nAll commits:")
    for commit in commits:
        print(
            f"{commit['timestamp'].strftime('%Y.%m.%d %I:%M%p')} - {commit['message']}"
        )


if __name__ == "__main__":
    if len(sys.argv) > 1:
        section = sys.argv[1]
        calculate_section_duration(section)
    else:
        list_all_sections()
