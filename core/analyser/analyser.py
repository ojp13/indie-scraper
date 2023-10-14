import pandas as pd
from pathlib import Path
import json

import plotly.express as px


def analyse_options(options):
    df = pd.DataFrame.from_dict(options)

    # df.set_index(["start_date", "start_city", "van"], inplace=True)

    df.drop(columns=["end_date", "end_city"], inplace=True)

    fig = px.scatter(
        df,
        x="start_date",
        y="total_price",
        color="van",
        hover_data=["van", "start_city", "total_price"],
    )

    fig.show()

    print(df)


if __name__ == "__main__":
    file_name = "results_20231014T091544.json"
    path = Path(".") / "results" / file_name

    with open(path, "r") as options_file:
        options = json.load(options_file)

    analyse_options(options)
