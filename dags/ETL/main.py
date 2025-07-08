from ETL import extract, transform, load

def run_etl():
    """
    Run the ETL process: extract, transform, and load data.
    """
    # Step 1: Extract data
    extract.extract_data()
    
    # Step 2: Transform data
    transform.read_csv()
    
    # Step 3: Load data

    load.upload_to_s3()



if __name__ == "__main__":
    run_etl()
    print("ETL process completed successfully.")