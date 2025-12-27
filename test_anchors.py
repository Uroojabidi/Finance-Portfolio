import re

def create_github_anchor(heading):
    # Remove emojis using regex
    emoji_pattern = re.compile(
        '['
        u'\U0001F600-\U0001F64F'  # emoticons
        u'\U0001F300-\U0001F5FF'  # symbols & pictographs
        u'\U0001F680-\U0001F6FF'  # transport & map symbols
        u'\U0001F1E0-\U0001F1FF'  # flags (iOS)
        u'\U00002640-\U00002642'  # gender symbols
        u'\U00002600-\U00002B55'  # misc symbols
        u'\U000023F0-\U000023FF'  # additional symbols
        u'\U0001F900-\U0001F9FF'  # supplemental symbols
        u'\U0001F018-\U0001F270'  # game symbols
        ']+',
        flags=re.UNICODE
    )
    
    clean_heading = emoji_pattern.sub('', heading)
    # Remove any remaining special characters except spaces
    clean_heading = re.sub(r'[^\w\s-]', '', clean_heading)
    # Replace multiple spaces with single space
    clean_heading = ' '.join(clean_heading.split())
    # Convert to lowercase and replace spaces with hyphens
    anchor = clean_heading.lower().replace(' ', '-')
    return anchor

# Test with our headings
headings = [
    '🎯 Why This Project Matters',
    '📋 Table of Contents', 
    '🎯 Project Overview',
    '👥 User Personas',
    '📁 Repository Structure',
    '🚀 Getting Started',
    '📊 Analysis Features',
    '📈 Sample Output',
    '🏗️ Architecture Diagram',
    '📚 Documentation Navigation',
    '📚 References (APA Format)',
    '🤝 Contributing',
    '📄 License',
    '⚠️ Ethics & Compliance'
]

for heading in headings:
    anchor = create_github_anchor(heading)
    print(f'Heading: {repr(heading.strip())} -> Anchor: #{anchor}')