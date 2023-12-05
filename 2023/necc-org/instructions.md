## Dependencies

### prod
```
fastapi
psycopg[binary]
redis
```
### dev
```
pytest
pytest-asyncio
httpx
uvicorn
mypy
```
###
```toml
[tool.pdm.scripts]
test = "pytest -ssvv"
run-dev = "pdm run uvicorn app.main:app --reload"
```
## DB schemas

* Create `category` table
```
id: UUUID
name: str
description: str | None = None
```

* Create `product` table
```
id: UUUID
name: str
price: float
description: str | None = None
category_id: UUUID
```
* Add FKEY to the category_id.

* Create Pydantic for the tables and request schemas.

## 