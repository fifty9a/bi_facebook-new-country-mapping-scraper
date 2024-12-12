# Facebook-New-Country-Mapping-File-Scraper
Repo for scraping Facebook's mapping files for new countries

### Installing required dependencies 
`pip install pandas`

### Running the Scraper

1. Open the `get_new_meta_mapping_files.ipynb` file and provide the script with the required params, to run the scrape.
User guide can be found here: [https://fifty9a.atlassian.net/wiki/spaces/BIK/pages/616726529/Meta+Audience+Scraper#Adding-support-for-new-countries]

### Current features

1. Check if Facebook Supports zipcode level mapping for the selected country
2. Check if Facebook Supports city level mapping for the selected country
3. Scrape mapping file at either zipcode / city level.

Note: Running the scrape at zipcode level will automatically include cities and regions too.
