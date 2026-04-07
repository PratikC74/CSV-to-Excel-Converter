import pandas as pd
import argparse
import logging
from utils import clean_data

#Setup logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def convert_csv_to_excel(input_file,output_file):
    try:
        logging.info(f"Reading file:{input_file}")

        #Read CSV

        df = pd.read_csv(input_file)

        #Clean data
        df = clean_data(df)

        #Save to excel
        df.to_excel(output_file,index=False,engine='openpyxl')

        logging.info(f"Successfully converted to {output_file}")
        print("Conversion Successfully")

    except FileNotFoundError:
        logging.error("File not found!")
        print("Error: Input file not found.")

    except Exception as e:
        logging.error(f"Error : {e}")
        print(f"Unexpected error:{e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CSV to Excel Converter")
    
    parser.add_argument("-i","--input",required=True,help="Input CSV file")
    parser.add_argument("-o","--output",required=True,help="Output CSV file")

    args = parser.parse_args()

    convert_csv_to_excel(args.input,args.output)
    