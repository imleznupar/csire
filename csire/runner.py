import argparse
from importlib.resources import path
import preprocess, filterInformation, extractCasualty, geoparser, generateMap
input_path = ""
country_code = ""

if __name__ == "__main__":
    parser = argparse.ArgumentParser("simple_example")
    parser.add_argument("input", help="input twarc csv file path", type=str)
    parser.add_argument("country", help="ISO 3166-1 alpha-3", type=str)
    
    args = parser.parse_args()
    input_path = args.input
    country_code = args.country
    print(input_path)
    print(country_code)

    x = preprocess.main(input_path)
    x = filterInformation.main(x)    
    x = extractCasualty.main(x)
    x = geoparser.main(x, country_code)
    x = generateMap.main(x)
