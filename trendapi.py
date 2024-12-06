import time
import csv
from pytrends.request import TrendReq
from datetime import datetime, timedelta

# 키워드 배열
keywords = ['비트코인', '이더리움', '업비트', '비트코인 시세', '빗썸']
start_date = datetime(2011, 1, 1)
end_date = datetime(2024, 11, 24)

# CSV 파일 경로
csv_file_path = "Trend.csv"

# 딜레이 함수 (초 단위)
def delay(seconds):
    time.sleep(seconds)

# 날짜 범위를 주 단위로 나누는 함수
def split_date_range(start_date, end_date, interval_days=7):
    date_ranges = []
    current_date = start_date
    while current_date < end_date:
        next_date = min(current_date + timedelta(days=interval_days), end_date)
        date_ranges.append((current_date, next_date))
        current_date = next_date
    return date_ranges

# Google Trends 데이터 수집
def fetch_trends_data():
    pytrends = TrendReq(hl='ko', tz=360)
    all_data_points = []

    for keyword in keywords:
        print(f"Fetching data for keyword: {keyword}")
        date_ranges = split_date_range(start_date, end_date)

        for start, end in date_ranges:
            timeframe = f"{start.strftime('%Y-%m-%d')} {end.strftime('%Y-%m-%d')}"
            try:
                pytrends.build_payload([keyword], cat=0, timeframe=timeframe, geo='KR')
                data = pytrends.interest_over_time()

                if not data.empty:
                    for date, row in data.iterrows():
                        if 'isPartial' in row and row['isPartial']:
                            continue
                        data_point = {
                            "date": date.strftime('%Y-%m-%d'),
                            "keyword": keyword,
                            "value": row[keyword],
                        }
                        all_data_points.append(data_point)
            except Exception as e:
                print(f"Error fetching data for {keyword} during {timeframe}: {e}")

            # 딜레이 추가
            delay(2)

    # CSV 파일로 저장
    save_to_csv(all_data_points)

# 데이터 저장 (CSV)
def save_to_csv(data_points):
    fieldnames = ['date', 'keyword', 'value']
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_points)
    print(f"Data saved to {csv_file_path}")

if __name__ == "__main__":
    fetch_trends_data()
