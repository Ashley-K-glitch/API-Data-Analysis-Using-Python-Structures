1. PROJECT OVERVIEW 
Pesa Pulse, a Nairobi fintech start-up, has just signed a partner who shares its customer directory through an API. Before the marketing team plans regional campaigns, they want to know the basics: how many customers there are, where they are, and what the data even looks like.

You are the junior analyst. Pull the data, explore its nested structure, extract the attributes that matter, and answer "where are our customers?" first with plain Python structures and then with pandas. Finish with a chart marketing can drop straight into a slide.

2. Project objectives
Learning objectives
Retrieve JSON from an API with requests and handle a failed request
Navigate nested dictionaries and lists confidently
Use sets to find unique values and dictionaries to count them
Write dict comprehensions for aggregation without pandas
Move the cleaned data into pandas, export it and visualise a distribution

3. Project Structure 
day1-api-analysis/
├── analysis.py            # or analysis.ipynb
├── output/
│   ├── customers.csv
│   ├── city_counts.csv
│   └── customer_distribution.png
├── requirements.txt
└── README.md

4. Workflow and methodology
Retrieved customer data with Requests
Explored nested dictionaries and lists
Extracted customer attributes
Used sets to find unique cities
Counted customers by city with loops
Convert the data into a DataFrame
Export the results to CSV
Visualise the customer distribution using cities
