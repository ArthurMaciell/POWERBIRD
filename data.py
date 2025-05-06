import requests
import pandas as pd
from datetime import datetime, timezone


page = 1
start_date = '2025-01-01'
end_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")



url = (
    f"https://crm.rdstation.com/api/v1/deals?page={page}"
    f"&limit=200&created_at_period=true&start_date={start_date}"
    f"T08%3A00%3A00&end_date={end_date}"
    f"T18%3A00%3A00&token=681a40c4468df10014d4bf51"
)

url1 = "https://crm.rdstation.com/api/v1/deals?page=1&limit=200&created_at_period=true&start_date=2025-01-01T08%3A00%3A00&end_date=2025-05-05T08%3A00%3A00&token=681a40c4468df10014d4bf51"
url2 = "https://crm.rdstation.com/api/v1/deals?created_at_start=2025-01-01&created_at_end=2025-05-06&page=1&limit=200"

print(end_date)
print(url)