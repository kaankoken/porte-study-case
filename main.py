from email import header
from typing import List, Tuple
import enum
import pandas as pd
import sys

from graph import Graph, printGraph
from path import Path


def main():
    arguments: List[str] = sys.argv[1:]
    if len(arguments) <= 0:
        print("Please provide a file path")
        sys.exit(0)

    if len(arguments) != 3:
        print("Please provide exactly 3 arguments")
        sys.exit(0)

    data: pd.DataFrame = pd.read_csv(arguments[0], sep=',')

    # Converting cities to lower case
    data['from_country'] = data['from_country'].apply(str.lower)
    data['to_country'] = data['to_country'].apply(str.lower)

    unique_countries: List[str] = list(data.from_country.unique())

    # Finding unique countries
    new_countries = [country for country in data.to_country.unique() if country not in unique_countries]

    unique_countries.extend(new_countries)
    unique_countries.sort()

    start = str.lower(arguments[1])
    end = str.lower(arguments[2])
    if start not in unique_countries or end not in unique_countries:
        print("Please provide valid countries")
        sys.exit(0)

    countries_enum: enum.Enum = enum.Enum('Countries', unique_countries, start=0)

    # Convering from_country, to_country to enum and adding to dataframe
    data['from_country_enum'] = data['from_country'].apply(lambda x: countries_enum[x].value)
    data['to_country_enum'] = data['to_country'].apply(lambda x: countries_enum[x].value)

    # Re-ordering columns
    order = ['from_country', 'from_country_enum', 'to_country', 'to_country_enum', 'cost', 'shipment_company']
    data = data.filter(order)

    # Creating tuple for graph
    data_to_list: List[Tuple[int]] = list(data.drop(
        columns=['from_country', 'to_country']).copy().itertuples(index=False, name=None),
        )

    graph = Graph(data_to_list, len(unique_countries))
    # printGraph(graph)

    # Dijkstra's algorithm
    path: Path = graph.dijkstra(countries_enum[start].value, countries_enum[end].value)
    path.result(countries_enum)


if __name__ == '__main__':
    main()
