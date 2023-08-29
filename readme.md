# Indie Campers Cost Scraping

A repo to use the Indie Campers API to scour for the best costs

```powershell
https://indiecampers.com/api/v3/availability
```

Example request payload

```json
{
    "booking":
    {
        "checkin_city":"orlando",
        "checkout_city":"orlando",
        "checkin_datetime":"2023-09-04T16:30:00+00:00",
        "checkout_datetime":"2023-10-16T11:00:00+00:00",
        "page":1,
        "locale":"gb",
        "van_categories":["sierra","conquest","ovation","applause","nomad-pop-top","four-winds","marco-polo","vw-california-premium","atlas-5","california","solis-air","sporty","atlas","nomad-ivy","nomad","metris","etrusco","active-plus","wrangler","tellaro","rebel","solis","vw-grand-california","california-manual","dawn-patrol","urban","explorer"]
    },
    "meta":
    {
        "current_route":"rent-an-rv-search"
    }
}
```

## Development

### Environment Setup

```powershell
python -m venv .venv
.venv/scripts/active
python -m pip install -e .[development]
```

### Launching in Debug Mode

```powershell
python -m debugpy --listen 5678 --wait-for-client .\core\scraper\scraper.py
```
