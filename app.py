from flask import Flask, render_template, request, flash
import pandas as pd

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flashing messages

# Load the dataset
df = pd.read_csv('data/superstore_sales.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Year'] = df['Order Date'].dt.year

# Get unique values for filters
categories = df['Category'].unique()
sub_categories = df['Sub-Category'].unique()
regions = df['Region'].unique()
segments = df['Segment'].unique()

@app.route('/', methods=['GET', 'POST'])
def index():
    query_result = None
    selected_category = request.form.get('category') if request.method == 'POST' else None
    selected_sub_category = request.form.get('sub_category') if request.method == 'POST' else None
    selected_region = request.form.get('region') if request.method == 'POST' else None
    selected_segment = request.form.get('segment') if request.method == 'POST' else None
    selected_query = request.form.get('query') if request.method == 'POST' else None

    if request.method == 'POST':
        # Validate conflicting selections
        if selected_category and selected_sub_category:
            sub_category_in_category = df[df['Category'] == selected_category]['Sub-Category'].unique()
            if selected_sub_category not in sub_category_in_category:
                flash('The selected Sub-Category does not belong to the selected Category. Please adjust your selection.')
                return render_template('index.html', categories=categories, sub_categories=sub_categories, 
                                       regions=regions, segments=segments, query_result=query_result, 
                                       selected_category=selected_category, selected_sub_category=selected_sub_category, 
                                       selected_region=selected_region, selected_segment=selected_segment, 
                                       selected_query=selected_query)

        # Filter the dataframe based on user selections
        filtered_df = df.copy()
        if selected_category:
            filtered_df = filtered_df[filtered_df['Category'] == selected_category]
        if selected_sub_category:
            filtered_df = filtered_df[filtered_df['Sub-Category'] == selected_sub_category]
        if selected_region:
            filtered_df = filtered_df[filtered_df['Region'] == selected_region]
        if selected_segment:
            filtered_df = filtered_df[filtered_df['Segment'] == selected_segment]

        # Run the selected query
        if selected_query == 'Total Sales and Profit':
            total_sales = filtered_df['Sales'].sum()
            total_profit = filtered_df['Profit'].sum()
            query_result = f'Total Sales: ${total_sales:.2f}, Total Profit: ${total_profit:.2f}'
        elif selected_query == 'Average Discount by Product':
            avg_discount = filtered_df.groupby('Product Name')['Discount'].mean().sort_values(ascending=False)
            query_result = avg_discount.to_frame().to_html()
        elif selected_query == 'Total Sales by Year':
            sales_by_year = filtered_df.groupby('Year')['Sales'].sum()
            query_result = sales_by_year.to_frame().to_html()
        elif selected_query == 'Profit by Region':
            profit_by_region = filtered_df.groupby('Region')['Profit'].sum()
            query_result = profit_by_region.to_frame().to_html()
        elif selected_query == 'Products with Negative Profit':
            negative_profit_products = filtered_df[filtered_df['Profit'] < 0]['Product Name'].unique()
            query_result = '<br>'.join(negative_profit_products)

    return render_template('index.html', categories=categories, sub_categories=sub_categories, 
                           regions=regions, segments=segments, query_result=query_result, 
                           selected_category=selected_category, selected_sub_category=selected_sub_category, 
                           selected_region=selected_region, selected_segment=selected_segment, 
                           selected_query=selected_query)

if __name__ == '__main__':
    app.run(debug=True)
