# **Web Scraper for News Headlines**

This is a simple Python script designed to scrape news headlines from a specified website and save them to a local text file.

## **Features**

* Fetches HTML content from a given URL using the *requests* library.  
* Parses the HTML to extract headlines using *BeautifulSoup*.  
* Saves all extracted headlines to a file named *headlines*.txt.  
* Includes a user-agent header to mimic a web browser, helping to bypass anti-scraping measures.

## **How to Run**

### **Prerequisites**

Before running the script, make sure you have the required Python libraries installed. You can install them using *pip*:

*pip install requests beautifulsoup4*

### **Usage**

1. Open your terminal or command prompt.  
2. Run the script by executing the following command:  
   *python web\_scraper.py*

3. The script will prompt you to enter a news website URL. If you press Enter without typing anything, it will default to scraping headlines from [*https://www.bbc.com/news*](https://www.bbc.com/news) .

### **Output**

The script will create a file named *headlines.txt* in the same directory, containing a list of the scraped headlines.

## **Customization**

You may need to modify the *soup.find\_all()* method in the script depending on the specific HTML structure of the website you want to scrape. Inspect the website's source code to find the correct HTML tags or classes for the headlines.