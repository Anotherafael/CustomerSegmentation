# Customer Segmentation and Profiling for Retail Store

## Abstract

The goal of this project is to better analyse and segment a retail store's client base in order to improve customer service and marketing tactics. To accomplish these objectives, I worked on a variety of data analysis and modelling activities for this project.

Understanding and defining the business challenge was the first step. I had to determine the significance of client segmentation for the retail establishment and the ways in which it may improve the targeting of marketing initiatives. I was able to comprehend the data, its structure, and the significance of each characteristic by thoroughly examining the dataset.

To ensure data quality, I cleaned the dataset by removing null and duplicated rows. After that, I dropped unnecessary features that did not contribute to the analysis. Data preprocessing was then conducted to prepare the data for Exploratory Data Analysis (EDA). During the EDA, I explored various aspects of the data, performed feature engineering, and analyzed outliers to identify patterns and insights.

After completing the EDA, I used K-Means to identify the most pertinent characteristics for the clustering model. I implemented feature encoding and scaling to enhance the model's performance. To further improve the clustering procedure and minimise dimensionality, Principal Component Analysis (PCA) was employed.

The K-Means model was built with five clusters using the preprocessed data, and I examined the traits and behaviours of each cluster. Lastly, I wrapped up the profiles of the clusters, offering the retail outlet practical advice on how to better customise their marketing plans and customer support initiatives.

Finally, a loyalty program was developed for the most valuable clients. This program aims to boost revenue by implementing strategies such as discounts, exclusive products, and targeted marketing campaigns. After defining the program, I projected potential financial outcomes to demonstrate its impact. The analysis showed a revenue increase of $125,674.50, representing a 9% growth.

I thoroughly loved working on this project and was able to show off my proficiency in doing in-depth data analysis and using machine learning approaches to address business challenges. I gained new skills and a deeper grasp of client segmentation and profiling from this amazing learning experience.

## Technologies

- Python (Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn)
- Jupyter Notebook
- Preprocessing (Feature Encoding, Feature Scaling, PCA)
- Machine Learning Clustering (K-Means, Elbow Method)
- Git

## 1. EDA

### 1.1 Dataset

We have a total of 28 features, excluding the ID. Among them, there are 2 categorical features and 26 numerical features.

**People:**

- ID: Customer's unique identifier
- Year_Birth: Customer's birth year
- Education: Customer's education level
- Marital_Status: Customer's marital status
- Income: Customer's yearly household income
- Kidhome: Number of children in customer's household
- Teenhome: Number of teenagers in customer's household
- Dt_Customer: Date of customer's enrollment with the company
- Recency: Number of days since customer's last purchase
- Complain: 1 if the customer complained in the last 2 years, 0 otherwise

**Products:**

- MntWines: Amount spent on wine in last 2 years
- MntFruits: Amount spent on fruits in last 2 years
- MntMeatProducts: Amount spent on meat in last 2 years
- MntFishProducts: Amount spent on fish in last 2 years
- MntSweetProducts: Amount spent on sweets in last 2 years
- MntGoldProds: Amount spent on gold in last 2 years

These product features represent the amounts spent on each type of product.

**Marketing Promotion:**

- NumDealsPurchases: Number of purchases made with a discount
- AcceptedCmp1: 1 if customer accepted the offer in the 1st campaign, 0 otherwise
- AcceptedCmp2: 1 if customer accepted the offer in the 2nd campaign, 0 otherwise
- AcceptedCmp3: 1 if customer accepted the offer in the 3rd campaign, 0 otherwise
- AcceptedCmp4: 1 if customer accepted the offer in the 4th campaign, 0 otherwise
- AcceptedCmp5: 1 if customer accepted the offer in the 5th campaign, 0 otherwise
- Response: 1 if customer accepted the offer in the last campaign, 0 otherwise

**Place:**

- NumWebPurchases: Number of purchases made through the company’s website
- NumCatalogPurchases: Number of purchases made using a catalogue
- NumStorePurchases: Number of purchases made directly in stores
- NumWebVisitsMonth: Number of visits to company’s website in the last month

### 1.2 RFM Model

I used the RFM model for clustering analysis.

The RFM model is a marketing and customer segmentation technique used to analyze and categorize customers based on their recent purchasing behavior.

![RFM Metrics](./assets/rfm/rfm_metrics.png)

By analyzing these three factors, businesses can categorize their customers into different segments, such as "high-value and highly engaged" or "low-value and inactive." This segmentation allows companies to tailor their marketing strategies and offers to each group more effectively, ultimately improving customer retention and maximizing revenue.

![RFM Map](./assets/rfm/rfm_map.png)

### 1.3 Conclusion

1. The product spending features are skewed to the right, meaning that while most customers spend less, some do so considerably more. Among all product categories, wine has the greatest average spending.

2. Features related to purchase frequency also show a little right skew. In general, consumers make more purchases in-person or online; outliers signify customers who make transactions frequently.

3. The efficacy of the store's existing initiatives is minimal, as only a tiny percentage of consumers participate in any given campaign. This emphasises how important clustering research is for more precise campaign targeting across client segments.

4. While some clients have no childs living at home, the majority has at least one. Few people have two kids. The majority of clients also have partners and are recent grads.

5. There is a substantial negative correlation between income and having children at home, indicating that consumers with higher incomes typically have fewer or no children, and vice versa.

6. Spending on pricey goods like wine and meat is positively correlated with income. Given that higher-income consumers typically buy these things more frequently.

7. Income and catalogue and in-store purchases have a high positive correlation, whereas monthly online visits and income have a negative correlation. This emphasises how crucial it is to improve higher-income customers' catalogue and in-store shopping experiences.

8. Customers with higher incomes are more inclined to participate in marketing initiatives.

9. There is a somewhat good correlation between having childs at home and looking for deals while making purchases.

10. The amount spent on different product kinds is strongly inversely correlated with monthly site visits, suggesting that these things are frequently bought through alternative channels like catalogues and storefronts. Additionally, there is a somewhat positive link with bargain purchases, indicating that regular users of the website have a tendency to buy things at a discount.

11. Higher-income consumers were successfully targeted by Campaigns 1 and 5, especially when it came to wine and meat purchases. Customers who made larger purchases showed a significantly greater proportion of marketing acceptance.

## 2. Clustering

The steps involved in the Clustering are:

- Elbow Method to determine the optimum number of clusters
- Employ the KMeans
- Examining the clusters

### 2.1 Elbow

The Elbow method indicates that 5 is to optimal number of clusters.

![Elbow](./assets/clustering/elbow.png)

### 2.2 Visualization

#### 2.2.1 3D Visualization of the clusters in the PCA results

![3D Clusters - PCA Features](./assets/clustering/3d_clusters_pca-features.png)

#### 2.2.2 2D Visualization of the clusters comparing the customers's income and total spent

![2D Clusters - Income vs. Total Spent](./assets/clustering/2d_clusters_income-totalspent.png)

#### 2.2.3 Visualization of the count for each Cluster

![Count of each cluster](./assets/clustering/countplot_clusters.png)

![Count of each cluster in Piechart](./assets/clustering/pie_count_clusters.png)

#### 2.2.4 Visualization of the differences in purchase types across clusters

![Clusters of purchases](./assets/clustering/purchases_clusters.png)

#### 2.2.5 Visualization of the differences in product types across clusters

![Clusters of products](./assets/clustering/products_clusters.png)

#### 2.2.6 Visualization of the differences in campaigns across clusters

![Clusters of campaings](./assets/clustering/campaings_clusters.png)

#### 2.2.7 Visualization of the revenue by each cluster

![Clusters of campaings](./assets/clustering/revenue_percentage_clusters.png)

### 2.3 Conclusion

#### Cluster 0 - "Prosperous Shoppers"

- Features the highest income and spending.
- Contains the smallest families, meaning that has no children.
- Mostly graduated, with some having completed postgraduate studies as well.
- Frequently makes purchases, with a strong preference for store and catalog shopping.
- Shows a significant expenditure on all types of products.
- Predominantly responds to campaign 1 and 5.
- A mix of old and middle-aged people, but having some young.
- Commonly don't use the web application.
- Recency: Highest.
- Frequency: High.

#### Cluster 1 - "Low Budget"

- Characterized by the lowest income and the lowest spending.
- Typically consists a small family.
- Mostly graduated, with a few having completed postgraduate studies as well.
- Rarely makes purchases, showing a high preference for deals.
- Purchases fewer products but shows a slight preference for food and gold products.
- Shows a low rate of campaign acceptance, with campaign 3 the most accepted.
- Commonly middle-aged people, and having the majority of young ones.
- Frequently uses the web application.
- Recency: High.
- Frequency: Lowest.

#### Cluster 2 - "Affluent Families"

- Exhibits the second highest income and spending.
- Typically consists of couples with one child.
- Mostly graduated, with many having completed postgraduate studies as well.
- Makes the highest number of purchases, without a strong preference for any specific shopping method.
- Shows significant expenditure for wines and gold items.
- Shows a low rate of campaign acceptance, with campaign 3 and 4 the most accepted.
- Commonly old people.
- Commonly don't use the web application.
- Recency: Low.
- Frequency: Highest.

#### Cluster 3 - "Web-Discount Seekers"

- Noted for the average income and spending.
- Comprises largest families.
- Mostly on graduated to postgraduate education levels.
- Often makes purchases, favoring deals and web shopping.
- Shows a decent expenditure with a preference over wines and gold products.
- Shows a low rate of campaign acceptance, with campaign 3 and 4 the most accepted.
- A mix of old and middle-aged people.
- Frequently uses the web application.
- Recency: Lowest.
- Frequency: High.

## 3. Loyalty Program

After analyzing the clusters, we can infere that the most valuable clients for a loyalty program are the Prosperous Shoppers, because they have:

- a high income;
- buys a lot of products;
- represent 49% of the total revenue.
- responds well to campaings.

### 3.1 Presumptions of Loyalty Program

- I assumed that the retail establishment can enhance the income of its Prosperous clientele by 15% by focused marketing efforts, customised merchandise, and exclusive deals.
- Since Prosperous and Affluent Families clients are comparable, I estimated a 30% conversion rate for Prosperous customers.
- Than, I assumed the following conversion rates to Prosperous, given that the other categories are more dissimilar from Prosperous customers: Web-Discount Seekers = 10% and Low Budget = 5%.

### 3.2 Results

- Total revenue before Prosperous loyalty program: $1,349,751.00.
- Total revenue after Prosperous loyalty program: $1,475,425.50
- Revenue increased by 9.00%
- Revenue increased in $125,674.50.
