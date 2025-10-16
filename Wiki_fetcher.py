import wikipedia

def get_wiki_summary():
    """
    Fetches and displays a summary of a Wikipedia article.
    """
    print("📚 Wikipedia Summary Fetcher 📚")
    
    query = input("Enter a topic you want to search on Wikipedia: ")

    try:
        print(f"\nSearching for '{query}'...")
        # Get the summary, automatically handling disambiguation
        summary = wikipedia.summary(query, sentences=5, auto_suggest=True)
        
        print("\n" + "="*20, "Summary", "="*20)
        print(summary)
        print("="*49)

    except wikipedia.exceptions.PageError:
        print(f"❌ Error: Could not find a Wikipedia page for '{query}'. Please try another topic.")
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"❌ Error: Your query is ambiguous. It could refer to one of the following:")
        for i, option in enumerate(e.options[:5]):
            print(f"  - {option}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    get_wiki_summary()
