# SKSkyforge - Sovereign Alignment Calendar

Daily cosmic alignment reports integrating moon phases, numerology,
Human Design, I Ching, biorhythms, and wellness recommendations.

## Install

```bash
pip install skskyforge
```

## Setup

Create a profile with your birth data:

```bash
skskyforge profile create --name default --birth-date 1985-03-15
```

Install daily 8am reports (systemd timer or crontab):

```bash
skskyforge install-daily
```

## Commands

- `skskyforge daily` -- generate today's full daily alignment report
- `skskyforge daily --format markdown --output file` -- save report to file
- `skskyforge preview --date YYYY-MM-DD` -- preview any day's alignment
- `skskyforge generate --year YYYY` -- generate full year calendar
- `skskyforge profile create/list/show/delete` -- manage user profiles
- `skskyforge install-daily --time HH:MM` -- install daily cron/timer
- `skskyforge uninstall-daily` -- remove daily cron/timer

## OpenClaw Integration

This skill is auto-discoverable by OpenClaw agents. When installed,
agents can invoke `skskyforge daily` to get the current day's alignment
data for context-aware responses.

## Author

smilinTux -- staycuriousANDkeepsmilin
