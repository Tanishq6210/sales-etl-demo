
import csv
import os
from collections import defaultdict
from pathlib import Path


def run_etl(input_file, output_file):
    totals = defaultdict(float)

    with open(input_file, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            totals[row["product"]] += (
                int(row["quantity"]) * float(row["price"])
            )

    print("Hi")
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["product", "total_sales"])

        for product, total in sorted(totals.items()):
            writer.writerow([product, round(total, 2)])

    print(f"ETL completed for environment: {os.getenv('APP_ENV', 'local')}")
    print(f"Output saved to {output_path}")


if __name__ == "__main__":
    run_etl(
        os.getenv("INPUT_FILE", "data/sales.csv"),
        os.getenv("OUTPUT_FILE", "output/sales_summary.csv"),
    )
