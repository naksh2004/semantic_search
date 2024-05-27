# metadata_extractor.py

def extract_metadata(text):
    # This is a simple example. You may need more sophisticated NLP techniques
    # to accurately extract metadata.
    title = text.split('\n')[0]  # Assuming the title is the first line
    industry = "Unknown"  # Extract industry from the text
    geography = "Unknown"  # Extract geography from the text
    use_case = "Unknown"  # Extract use case from the text
    return {
        "title": title,
        "industry": industry,
        "geography": geography,
        "use_case": use_case
    }
