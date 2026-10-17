
import csv

from etl import run_etl


def test_sales_etl(tmp_path):
    source = tmp_path / "sales.csv"
    output = tmp_path / "summary.csv"

    source.write_text(
        "product,quantity,price\n"
        "Laptop,2,100\n"
        "Laptop,1,100\n"
        "Mouse,3,10\n",
        encoding="utf-8",
    )

    run_etl(source, output)

    with output.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert rows == [
        {"product": "Laptop", "total_sales": "300.0"},
        {"product": "Mouse", "total_sales": "30.0"},
    ]
