# SKSkyforge CLI Quickstart

> Get up and running with your first sovereign alignment calendar in under 5 minutes.

## Install

```bash
pip install skskyforge
```

Or from source:

```bash
git clone https://github.com/smilinTux/SKyForge.git
cd SKyForge
pip install -e ".[all]"         # geocoding + all optional extras
```

The `[all]` extra pulls in `geopy` and `timezonefinder` for automatic
location geocoding. Without it the core calendar still works — you just
won't get coordinates or auto-detected timezones.

## 1. Create a Profile

A profile stores your birth data so every calendar is personalised.

```bash
# Minimal — just name and date
skskyforge profile create \
  --name luna \
  --birth-date 1992-06-21

# Full — exact time + city (auto-geocoded)
skskyforge profile create \
  --name luna \
  --birth-date 1992-06-21 \
  --birth-time 14:30 \
  --birth-location "Austin, TX"
```

When you pass `--birth-location`, SKSkyforge geocodes the city
automatically via OpenStreetMap and stores the latitude, longitude, and
IANA timezone (e.g. `America/Chicago`) in your profile.

If geocoding is unavailable (no network or missing `geopy`), the city
name is stored as-is with a `UTC` fallback timezone.

### Manage profiles

```bash
skskyforge profile list           # table of all profiles
skskyforge profile show luna      # full profile details
skskyforge profile delete luna    # remove a profile
```

## 2. Preview a Single Day

```bash
skskyforge preview --date 2026-03-20 --profile luna
```

This prints a rich terminal report covering all 10 domains: moon phase
and sign, numerology, biorhythm cycles, risk analysis, exercise,
nourishment, and spiritual reading — all tuned to the profile's birth
data.

## 3. Generate a Calendar

```bash
# Full year — JSON output (default)
skskyforge generate --year 2026 --profile luna

# Single month — PDF
skskyforge generate --year 2026 --month 3 --format pdf

# Multiple formats at once
skskyforge generate --year 2026 --format json --format excel

# Custom output directory
skskyforge generate --year 2026 --output ~/calendars/
```

Supported formats: `json`, `pdf`, `excel`, `csv`.

## 4. Daily Report

Get today's alignment printed to your terminal — perfect for a morning
routine or automation:

```bash
skskyforge daily                                  # defaults
skskyforge daily --profile luna --format markdown  # markdown output
skskyforge daily --format json --output file       # save to file
```

### Automate with a timer

```bash
# Install a systemd timer (Linux) / launchd plist (macOS) / Task Scheduler (Windows)
skskyforge install-daily --time 07:30 --profile luna

# Remove it later
skskyforge uninstall-daily
```

The installer picks the best scheduler for your OS automatically:
- **Linux**: systemd user timer, crontab fallback
- **macOS**: launchd plist, crontab fallback
- **Windows**: `schtasks`

## CLI Reference

| Command | Description |
|---------|-------------|
| `skskyforge generate` | Generate a full or monthly calendar |
| `skskyforge preview` | Preview a single day's alignment report |
| `skskyforge daily` | Print today's report (non-interactive) |
| `skskyforge install-daily` | Schedule an automatic daily report |
| `skskyforge uninstall-daily` | Remove the scheduled daily report |
| `skskyforge profile create` | Create a new user profile |
| `skskyforge profile list` | List all profiles |
| `skskyforge profile show NAME` | Show profile details |
| `skskyforge profile delete NAME` | Delete a profile |
| `skskyforge --version` | Show version |

### Global options

Every command accepts `--help` for detailed usage. Profile commands
default to `default` if `--profile` is not specified.

## Configuration

SKSkyforge stores all user data under `~/.skskyforge/`:

```
~/.skskyforge/
├── profiles/       # YAML profile files
├── output/         # generated calendars
└── settings.yaml   # optional overrides
```

### Environment variables

| Variable | Purpose |
|----------|---------|
| `SKSKYFORGE_OUTPUT_DIR` | Override output directory |
| `SKSKYFORGE_DEFAULT_PROFILE` | Default profile name |
| `SWISSEPH_PATH` | Swiss Ephemeris data directory |

## The 10 Domains

Each day's report integrates guidance from all 10 domains:

1. **Moon Phase & Sign** — lunar phase, zodiac position, void-of-course windows
2. **Numerology** — life path, personal year / month / day numbers
3. **Solar Return** — annual chart focus, planetary transits
4. **Human Design** — type, strategy, authority, daily gate activations
5. **I Ching** — daily hexagram overlay with line-level wisdom
6. **Biorhythm** — physical, emotional, and intellectual cycles
7. **Risk Analysis** — multi-domain risk scoring and warnings
8. **Exercise & Embodiment** — element-tuned physical activity picks
9. **Nourishment** — dietary guidance matched to elemental energies
10. **Spiritual Reading** — curated daily wisdom text rotation

---

*Scientifically mapped. Spiritually grounded.*
