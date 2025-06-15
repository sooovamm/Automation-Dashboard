def google_search():
        from googlesearch import search

        query = "Python programming"  # Replace with your query

        # Fetch the first 5 pages of search results
        search_results = search(query, num_results=5)

        # Print the title and URL of each search result
        for i, result in enumerate(search_results, start=1):
            print(f"Result {i}:")
            print(result)
            print()
