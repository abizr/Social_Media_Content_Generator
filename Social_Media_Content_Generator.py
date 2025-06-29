import streamlit as st
import sqlite3
import json
import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
import random
import re
import requests


# Data Classes (OOP - Encapsulation of data)
@dataclass
class SocialMediaPost:
    """Data class representing a social media post."""
    id: Optional[int] = None
    text: str = ""
    hashtags: List[str] = None
    platform: str = ""
    tone: str = ""
    content_type: str = ""
    timestamp: str = ""
    
    def __post_init__(self):
        if self.hashtags is None:
            self.hashtags = []
        if not self.timestamp:
            self.timestamp = datetime.datetime.now().isoformat()


@dataclass
class UserSettings:
    """Data class for user preferences and settings."""
    default_tone: str = "professional"
    default_platforms: List[str] = None
    api_key: str = ""
    
    def __post_init__(self):
        if self.default_platforms is None:
            self.default_platforms = ["Facebook", "Twitter"]


# Core Classes (OOP - Encapsulation of functionality)
class ContentGenerator:
    """Class responsible for generating social media content using AI models."""
    
    def __init__(self):
        self.platform_limits = {
            "Twitter": 280,
            "Facebook": 2000,
            "Instagram": 2200,
            "LinkedIn": 3000
        }
        
        # Sample content templates for demonstration (in real implementation, this would use actual AI models)
        self.content_templates = {
            "promotional": [
                "🚀 Exciting news! {topic} is here to revolutionize your experience. Don't miss out on this amazing opportunity!",
                "✨ Discover the power of {topic}! Join thousands of satisfied customers who have already transformed their lives.",
                "🎯 Ready to take your {topic} to the next level? Our solution is exactly what you've been looking for!"
            ],
            "informative": [
                "Did you know that {topic} can significantly impact your daily routine? Here are some key insights to consider.",
                "Understanding {topic} is crucial in today's world. Let's explore the facts and benefits together.",
                "📊 Research shows that {topic} plays a vital role in modern business. Here's what you need to know."
            ],
            "question": [
                "What's your experience with {topic}? We'd love to hear your thoughts and stories!",
                "How has {topic} changed your perspective? Share your insights in the comments below!",
                "🤔 What would you do if {topic} wasn't available? Let's discuss the alternatives!"
            ]
        }
        
        self.tone_modifiers = {
            "professional": "maintaining a professional and authoritative tone",
            "casual": "using a friendly and conversational approach",
            "humorous": "adding a touch of humor and playfulness",
            "empathetic": "showing understanding and emotional connection"
        }
    
    def generate_text_post(self, topic: str, content_type: str, platform: str, tone: str, cta: str = "") -> str:
        """
        Generate a text post based on input parameters.
        
        Args:
            topic: Main subject of the post
            content_type: Type of content (promotional, informative, question)
            platform: Target social media platform
            tone: Desired tone of voice
            cta: Call to action (optional)
        
        Returns:
            Generated text post
        """
        # Select template based on content type (using data structures - dictionary lookup)
        templates = self.content_templates.get(content_type, self.content_templates["informative"])
        
        # Randomly select a template (demonstrating list indexing)
        base_template = random.choice(templates)
        
        # Generate content by replacing placeholder
        generated_text = base_template.format(topic=topic)
        
        # Apply tone modifications (demonstrating string manipulation and conditionals)
        if tone == "humorous":
            generated_text += " 😄"
        elif tone == "professional":
            generated_text = generated_text.replace("!", ".")
        
        # Add call to action if provided
        if cta:
            generated_text += f" {cta}"
        
        # Ensure content fits platform limits (demonstrating looping and string manipulation)
        platform_limit = self.platform_limits.get(platform, 2000)
        if len(generated_text) > platform_limit:
            # Truncate and add ellipsis
            generated_text = generated_text[:platform_limit-3] + "..."
        
        return generated_text


class HashtagSuggester:
    """Class responsible for suggesting relevant hashtags."""
    
    def __init__(self):
        # Sample hashtag database (in real implementation, this would use NLP models)
        self.hashtag_database = {
            "business": ["#business", "#entrepreneur", "#startup", "#success", "#growth"],
            "technology": ["#tech", "#innovation", "#digital", "#AI", "#future"],
            "marketing": ["#marketing", "#socialmedia", "#branding", "#content", "#strategy"],
            "health": ["#health", "#wellness", "#fitness", "#lifestyle", "#selfcare"],
            "education": ["#education", "#learning", "#knowledge", "#skills", "#development"]
        }
        
        self.trending_hashtags = ["#trending", "#viral", "#popular", "#2025", "#new"]
    
    def suggest_hashtags(self, text: str, count: int = 5) -> List[str]:
        """
        Suggest hashtags based on the input text.
        
        Args:
            text: Input text to analyze
            count: Number of hashtags to suggest
        
        Returns:
            List of suggested hashtags
        """
        suggested_hashtags = set()  # Using set data structure to avoid duplicates
        text_lower = text.lower()
        
        # Loop through hashtag database to find relevant hashtags
        for category, hashtags in self.hashtag_database.items():
            if category in text_lower:
                # Add hashtags from matching category (demonstrating list extension)
                suggested_hashtags.update(hashtags[:3])  # Limit to 3 per category
        
        # Add some trending hashtags (demonstrating random selection from list)
        suggested_hashtags.update(random.sample(self.trending_hashtags, min(2, len(self.trending_hashtags))))
        
        # Convert set back to list and limit to requested count
        hashtag_list = list(suggested_hashtags)[:count]
        
        # If we don't have enough hashtags, add generic ones
        while len(hashtag_list) < count:
            generic_hashtags = ["#content", "#social", "#post", "#share", "#engage"]
            for hashtag in generic_hashtags:
                if hashtag not in hashtag_list:
                    hashtag_list.append(hashtag)
                    if len(hashtag_list) >= count:
                        break
        
        return hashtag_list[:count]


class ImageIdeaGenerator:
    """Class responsible for generating image ideas/prompts."""
    
    def __init__(self):
        self.image_styles = [
            "professional photography",
            "minimalist design",
            "vibrant colors",
            "modern illustration",
            "infographic style"
        ]
        
        self.image_elements = [
            "people working together",
            "technology devices",
            "abstract concepts",
            "nature elements",
            "geometric shapes"
        ]
    
    def generate_ideas(self, text_post: str) -> List[str]:
        """
        Generate image ideas based on the text post.
        
        Args:
            text_post: The generated text post
        
        Returns:
            List of image idea descriptions
        """
        ideas = []
        
        # Analyze text for keywords (simple keyword extraction)
        keywords = self._extract_keywords(text_post)
        
        # Generate ideas by combining styles and elements (demonstrating nested loops)
        for i, style in enumerate(self.image_styles[:3]):  # Limit to 3 styles
            for j, element in enumerate(self.image_elements[:2]):  # Limit to 2 elements per style
                if keywords:
                    # Incorporate keywords into the idea
                    idea = f"{style.title()} featuring {element} related to {', '.join(keywords[:2])}"
                else:
                    idea = f"{style.title()} featuring {element}"
                ideas.append(idea)
                
                if len(ideas) >= 5:  # Limit total ideas
                    break
            if len(ideas) >= 5:
                break
        
        return ideas
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extract keywords from text (simplified implementation)."""
        # Remove common words and extract meaningful terms
        common_words = {"the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "by"}
        words = re.findall(r'\b\w+\b', text.lower())
        keywords = [word for word in words if len(word) > 3 and word not in common_words]
        return keywords[:5]  # Return top 5 keywords


class PostRepository:
    """Class responsible for database operations (Repository pattern)."""
    
    def __init__(self, db_path: str = "social_media_posts.db"):
        self.db_path = db_path
        self._initialize_database()
    
    def _initialize_database(self):
        """Initialize the SQLite database with required tables."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create posts table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT NOT NULL,
                    hashtags TEXT,
                    platform TEXT,
                    tone TEXT,
                    content_type TEXT,
                    timestamp TEXT
                )
            """)
            
            # Create settings table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_settings (
                    id INTEGER PRIMARY KEY,
                    default_tone TEXT,
                    default_platforms TEXT,
                    api_key TEXT
                )
            """)
            
            conn.commit()
    
    def save_post(self, post: SocialMediaPost) -> int:
        """Save a post to the database."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO posts (text, hashtags, platform, tone, content_type, timestamp)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                post.text,
                json.dumps(post.hashtags),  # Store list as JSON string
                post.platform,
                post.tone,
                post.content_type,
                post.timestamp
            ))
            conn.commit()
            return cursor.lastrowid
    
    def get_all_posts(self) -> List[SocialMediaPost]:
        """Retrieve all posts from the database."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM posts ORDER BY timestamp DESC")
            rows = cursor.fetchall()
            
            posts = []
            # Loop through database results and convert to objects (demonstrating iteration)
            for row in rows:
                post = SocialMediaPost(
                    id=row[0],
                    text=row[1],
                    hashtags=json.loads(row[2]) if row[2] else [],
                    platform=row[3],
                    tone=row[4],
                    content_type=row[5],
                    timestamp=row[6]
                )
                posts.append(post)
            
            return posts
    
    def delete_post(self, post_id: int):
        """Delete a post from the database."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM posts WHERE id = ?", (post_id,))
            conn.commit()
    
    def save_settings(self, settings: UserSettings):
        """Save user settings to the database."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO user_settings (id, default_tone, default_platforms, api_key)
                VALUES (1, ?, ?, ?)
            """, (
                settings.default_tone,
                json.dumps(settings.default_platforms),
                settings.api_key
            ))
            conn.commit()
    
    def load_settings(self) -> UserSettings:
        """Load user settings from the database."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user_settings WHERE id = 1")
            row = cursor.fetchone()
            
            if row:
                return UserSettings(
                    default_tone=row[1],
                    default_platforms=json.loads(row[2]) if row[2] else ["Facebook", "Twitter"],
                    api_key=row[3] or ""
                )
            else:
                return UserSettings()  # Return default settings

# Link documentation OpenRouter model for free LLM [list_model](https://openrouter.ai/models/?q=free)
# LLM Service for OpenRouter API (Free LLM)
class LLMService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.model = "deepseek/deepseek-chat-v3-0324"  # Use the recommended free model

    def generate_content(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}]
        }
        try:
            response = requests.post(self.api_url, headers=headers, json=data, timeout=30)
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            else:
                return f"Error: {response.text}"
        except Exception as e:
            return f"Error: {str(e)}"


# Streamlit Application
def main():
    """Main Streamlit application function."""
    st.set_page_config(
        page_title="AI Social Media Content Generator",
        page_icon="🚀",
        layout="wide"
    )

    # Add a logo
    st.image("C:\\Users\\Lenovo\\Project AI Python Bootcamp Skill Academy\\fin_pro\\image\\logo me.png", width=500)

    # Custom theme (Streamlit theme config is in .streamlit/config.toml, but we can use markdown for some tweaks)
    st.markdown("""
        <style>
        .main {background-color: #f5f7fa;}
        .stButton>button {background-color: #4F8BF9; color: white; font-weight: bold;}
        .stTabs [data-baseweb="tab"] {font-size: 18px;}
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

    # --- THEME TOGGLE (LIGHT/DARK MODE) ---
    theme = st.session_state.get('theme', 'light')
    theme_toggle = st.toggle("🌗 Toggle Dark/Light Mode", value=(theme == 'dark'))
    if theme_toggle:
        theme = 'dark'
    else:
        theme = 'light'
    st.session_state['theme'] = theme
    # Apply theme styles
    if theme == 'dark':
        st.markdown("""
            <style>
            .main {background-color: #18191a; color: #f5f7fa;}
            .stButton>button {background-color: #222; color: #f5f7fa;}
            .stTabs [data-baseweb="tab"] {color: #f5f7fa;}
            .stTextInput>div>div>input, .stTextArea textarea {background: #222; color: #f5f7fa;}
            .stSelectbox>div>div>div>div {background: #222; color: #f5f7fa;}
            .stMultiSelect>div>div>div>div {background: #222; color: #f5f7fa;}
            .stExpanderHeader {color: #f5f7fa;}
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            .main {background-color: #fff; color: #222;}
            .stButton>button {background-color: #4F8BF9; color: #fff;}
            .stTabs [data-baseweb="tab"] {color: #222;}
            .stTextInput>div>div>input, .stTextArea textarea {background: #f5f7fa; color: #222;}
            .stSelectbox>div>div>div>div {background: #f5f7fa; color: #222;}
            .stMultiSelect>div>div>div>div {background: #f5f7fa; color: #222;}
            .stExpanderHeader {color: #222;}
            </style>
        """, unsafe_allow_html=True)

    # Initialize session state for objects (demonstrating state management)
    if 'content_generator' not in st.session_state:
        st.session_state.content_generator = ContentGenerator()
    if 'hashtag_suggester' not in st.session_state:
        st.session_state.hashtag_suggester = HashtagSuggester()
    if 'image_idea_generator' not in st.session_state:
        st.session_state.image_idea_generator = ImageIdeaGenerator()
    if 'post_repository' not in st.session_state:
        st.session_state.post_repository = PostRepository()
    if 'llm_service' not in st.session_state:
        api_key = st.session_state.post_repository.load_settings().api_key
        st.session_state.llm_service = LLMService(api_key) if api_key else None

    # Load user settings
    user_settings = st.session_state.post_repository.load_settings()

    # Tabs for navigation
    tab1, tab2, tab3 = st.tabs(["Content Generator", "Content History", "Settings"])
    with tab1:
        content_generator_page(user_settings, theme)
    with tab2:
        content_history_page()
    with tab3:
        settings_page()

    # Footer
    st.markdown("""
        <hr>
        <div style='text-align:center;'>
        Developer by Abizar Al Gifari Rahman 😎 | <a href='https://www.linkedin.com/in/abizar-al-gifari/' target='_blank'>LinkedIn</a>
        </div>
    """, unsafe_allow_html=True)


def content_generator_page(user_settings: UserSettings, theme: str):
    """Main content generation page."""
    st.header("Generate Social Media Content")

    # Create two columns for better layout
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Content Parameters")

        # Input forms (demonstrating various Streamlit widgets)
        topic = st.text_area(
            "Topic/Keywords",
            placeholder="Enter the main topic or keywords for your post...",
            help="Describe what you want to post about"
        )

        content_type = st.selectbox(
            "Content Type",
            ["promotional", "informative", "question"],
            help="Choose the type of content you want to generate"
        )

        platforms = st.multiselect(
            "Target Platforms",
            ["Facebook", "Twitter", "Instagram", "LinkedIn"],
            default=user_settings.default_platforms,
            help="Select the social media platforms for this post"
        )

        tone = st.selectbox(
            "Tone of Voice",
            ["professional", "casual", "humorous", "empathetic"],
            index=["professional", "casual", "humorous", "empathetic"].index(user_settings.default_tone),
            help="Choose the tone for your content"
        )

        cta = st.text_input(
            "Call to Action (Optional)",
            placeholder="e.g., Learn More, Shop Now, Sign Up...",
            help="Add a specific call to action"
        )

        use_llm = st.checkbox("Use AI LLM (OpenRouter)", value=False, help="Generate content using a real AI model (requires API key in settings)")

        # Unified button for both content and complex caption/idea
        if st.button("✨ Generate Comprehensive Content"):
            if topic.strip():
                generate_comprehensive_content(topic, content_type, platforms, tone, cta, use_llm, theme)
            else:
                st.error("Please enter a topic or keywords!")

    with col2:
        st.subheader("Tips")
        st.info("""
        💡 **Tips for better content:**
        - Be specific with your topic
        - Choose the right tone for your audience
        - Consider platform-specific requirements
        - Add relevant call-to-actions
        """)
        st.success("Try the new AI LLM feature for more creative content!")


def generate_comprehensive_content(topic: str, content_type: str, platforms: List[str], tone: str, cta: str, use_llm: bool = False, theme: str = 'light'):
    """Generate and display comprehensive content: posts, hashtags, image ideas, and complex caption/idea."""
    with st.spinner("Generating your content..."):
        # Generate posts
        generated_posts = {}
        if use_llm and st.session_state.llm_service:
            prompt = f"Generate a {content_type} social media post about '{topic}' for the following platforms: {', '.join(platforms)}. Use a {tone} tone. Call to action: {cta if cta else 'None'}. Return a post for each platform."
            ai_content = st.session_state.llm_service.generate_content(prompt)
            for platform in platforms:
                if platform in ai_content:
                    start = ai_content.find(platform)
                    end = ai_content.find('\n', start)
                    post_text = ai_content[start+len(platform):end].strip() if end > start else ai_content[start+len(platform):].strip()
                    generated_posts[platform] = post_text
                else:
                    generated_posts[platform] = ai_content
        else:
            for platform in platforms:
                generated_text = st.session_state.content_generator.generate_text_post(
                    topic, content_type, platform, tone, cta
                )
                generated_posts[platform] = generated_text

        sample_text = list(generated_posts.values())[0] if generated_posts else topic
        hashtags = st.session_state.hashtag_suggester.suggest_hashtags(sample_text)

        # Improved image/photo idea generation
        if use_llm and st.session_state.llm_service:
            image_prompt = (
                f"Given the topic '{topic}', content type '{content_type}', and tone '{tone}', "
                f"generate 3-5 creative, visually descriptive image or photo ideas that would be perfect to accompany a social media post. "
                f"Each idea should have a short, catchy title and a detailed, vivid, and actionable description (at least 2 sentences). "
                f"Format as a numbered list, with each item as 'Title: Description'."
            )
            image_ideas_raw = st.session_state.llm_service.generate_content(image_prompt)
            image_ideas = [line.strip(" .-") for line in image_ideas_raw.split('\n') if line.strip() and any(c.isalpha() for c in line)]
        else:
            # Enhanced template fallback with more detailed descriptions
            base_ideas = [
                f"Engaging Group: A high-quality photo of people actively engaging with {topic} in a {tone} setting, showing real emotions and dynamic interaction. The background should be lively and relevant to the topic, with natural lighting and candid expressions.",
                f"Modern Minimalist: A modern, minimalist illustration representing {topic} and its impact, using bold colors and simple shapes. The design should highlight the core message and be easily shareable on social media.",
                f"Vivid Infographic: A vibrant infographic showing key facts about {topic}, with icons, charts, and concise text. The layout should be visually balanced and easy to read, drawing attention to the most important data.",
                f"Creative Flat-lay: A creative flat-lay of objects or symbols related to {topic}, arranged neatly on a contrasting background. The photo should use top-down perspective and include props that reinforce the message.",
                f"Dynamic Scene: A dynamic scene showing the benefits of {topic} for the audience, with people in action, expressive gestures, and a clear focal point. The setting should be aspirational and relatable."
            ]
            image_ideas = [idea.replace('{topic}', topic).replace('{tone}', tone) for idea in base_ideas][:5]

        # Generate complex caption & idea
        if use_llm and st.session_state.llm_service:
            prompt = (
                f"Generate a creative social media package for the topic '{topic}'.\n"
                f"Format the response as follows:\n"
                f"1. Caption (short, catchy, max 20 words)\n"
                f"2. Post Idea (detailed, creative, 2-3 sentences)\n"
                f"3. Suggested Hashtags (5, comma separated)\n"
                f"4. Visual/Design Suggestion (describe an image or design to accompany the post)\n"
                f"Content type: {content_type}, Tone: {tone}, Call to action: {cta if cta else 'None'}."
            )
            complex_result = st.session_state.llm_service.generate_content(prompt)
        else:
            caption = f"{topic.title()} - {random.choice(['Unleash the Possibilities!', 'Your Next Big Move!', 'Level Up Today!'])}"
            idea = f"Share insights about {topic} in a {tone} way. Encourage your audience to engage and take action."
            hashtags_complex = ', '.join(random.sample(['#Inspire', '#Growth', '#Now', '#SocialTips', '#Engage', '#Trendy', '#Viral', '#Success', '#Create', '#Share'], 5))
            visual = f"A vibrant, eye-catching graphic featuring {topic} and a call-to-action button."
            complex_result = f"1. Caption: {caption}\n2. Post Idea: {idea}\n3. Suggested Hashtags: {hashtags_complex}\n4. Visual/Design Suggestion: {visual}"

    # Show a simple effect (not balloons) if successful
    st.toast("Content generated successfully!", icon="✅")

    st.subheader("Generated Posts")
    for platform, text in generated_posts.items():
        with st.expander(f"📱 {platform} Post"):
            st.text_area(f"{platform} Content", text, height=100, key=f"text_{platform}")
            if st.button(f"💾 Save {platform} Post", key=f"save_{platform}"):
                post = SocialMediaPost(
                    text=text,
                    hashtags=hashtags.copy(),
                    platform=platform,
                    tone=tone,
                    content_type=content_type
                )
                post_id = st.session_state.post_repository.save_post(post)
                st.success(f"Post saved with ID: {post_id}")

    # --- IMPROVED SUGGESTED HASHTAGS SECTION ---
    st.subheader("Suggested Hashtags")
    # Improved hashtag generation with LLM or fallback
    if use_llm and st.session_state.llm_service:
        hashtag_prompt = (
            f"Generate a list of 7-10 highly relevant, trending, and platform-optimized hashtags for a social media post about '{topic}'. "
            f"The hashtags should maximize reach, engagement, and discoverability, mixing broad, niche, and branded tags. "
            f"Avoid banned or overused hashtags. Tailor them for these platforms: {', '.join(platforms)}. "
            f"Return only the hashtags, each starting with #, separated by spaces or newlines."
        )
        hashtags_raw = st.session_state.llm_service.generate_content(hashtag_prompt)
        # Extract hashtags using regex
        hashtags = re.findall(r"#\w+", hashtags_raw)
        hashtags = list(dict.fromkeys(hashtags))[:10]  # Remove duplicates, limit to 10
    else:
        # Enhanced fallback: extract keywords from generated post, combine with curated impactful hashtags
        def extract_keywords(text):
            common = {"the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "by", "is", "are", "this", "that", "from", "about", "your", "you", "our", "their", "it's", "its"}
            words = re.findall(r'\b\w+\b', text.lower())
            return [w for w in words if len(w) > 3 and w not in common]
        keywords = extract_keywords(sample_text)
        curated = [
            "#Viral", "#TrendingNow", "#MustSee", "#Inspiration", "#SocialMedia", "#GrowthHacks", "#BrandAwareness", "#Engage", "#ContentStrategy", "#ExplorePage"
        ]
        hashtags = [f"#{k.title().replace(' ', '')}" for k in keywords[:5]] + random.sample(curated, 5)
        hashtags = list(dict.fromkeys(hashtags))[:10]
    # Display hashtags as a bullet list and in a copyable text area
    st.markdown("**These hashtags are selected to boost reach and engagement:**")
    for tag in hashtags:
        st.markdown(f"- {tag}")
    hashtag_text = " ".join(hashtags)
    st.text_area("Copy Hashtags", hashtag_text, height=68)

    st.subheader("Image/Photo Ideas")
    # Display only the idea title as a bullet, description as plain text (indented, no bullet)
    def split_title_desc(line):
        # Try to split into title and description by common separators
        for sep in [": ", " - ", " – ", " — ", ". "]:
            if sep in line:
                parts = line.split(sep, 1)
                return parts[0].strip(), parts[1].strip()
        return line.strip(), None
    if use_llm and st.session_state.llm_service:
        cleaned_ideas = []
        def is_idea_line(line):
            # Consider a line an idea if it contains at least 3 words and some alphabetic characters
            return len(line.split()) >= 3 and any(c.isalpha() for c in line)

        for idea in image_ideas:
            cleaned = idea.lstrip("0123456789. -").strip()
            if is_idea_line(cleaned):
                cleaned_ideas.append(cleaned)
        for idea in cleaned_ideas:
            title, desc = split_title_desc(idea)
            st.markdown(f"- {title}")
            if desc:
                st.markdown(f"<div style='margin-left:24px;color:gray;font-size:0.95em'>{desc}</div>", unsafe_allow_html=True)
    else:
        for idea in image_ideas:
            title, desc = split_title_desc(idea)
            st.markdown(f"- {title}")
            if desc:
                st.markdown(f"<div style='margin-left:24px;color:gray;font-size:0.95em'>{desc}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("✨ Complex Caption & Idea (Comprehensive)")
    # Parse and display the complex_result as bullet points, no extra description
    def parse_complex_result(text):
        result = {'Caption': '', 'Post Idea': '', 'Hashtags': '', 'Visual/Design Suggestion': ''}
        import re
        text = re.sub(r"\n?\d+\.\s*", "\n", text)
        for key in result.keys():
            pattern = rf"{key}[:\s]*([^\n]*)"
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                result[key] = match.group(1).strip()
        return result
    parsed = parse_complex_result(complex_result)
    st.markdown(f"""
    <div style='background-color:{'#23272e' if theme == 'dark' else '#f0f4fa'};padding:16px;border-radius:10px;'>
    <ul style='margin:0 0 0 18px;padding:0;'>
      <li><b>Caption:</b> {parsed['Caption']}</li>
      <li><b>Post Idea:</b> {parsed['Post Idea']}</li>
      <li><b>Hashtags:</b> {parsed['Hashtags']}</li>
      <li><b>Visual/Design Suggestion:</b> {parsed['Visual/Design Suggestion']}</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)


def content_history_page():
    """Display saved content history."""
    st.header("Content History")
    
    # Load all posts
    posts = st.session_state.post_repository.get_all_posts()
    
    if not posts:
        st.info("No saved posts yet. Generate some content first!")
        return
    
    # Filter options
    col1, col2 = st.columns(2)
    with col1:
        platform_filter = st.selectbox(
            "Filter by Platform",
            ["All"] + ["Facebook", "Twitter", "Instagram", "LinkedIn"]
        )
    
    with col2:
        tone_filter = st.selectbox(
            "Filter by Tone",
            ["All"] + ["professional", "casual", "humorous", "empathetic"]
        )
    
    # Apply filters (demonstrating list comprehension and conditional logic)
    filtered_posts = posts
    if platform_filter != "All":
        filtered_posts = [post for post in filtered_posts if post.platform == platform_filter]
    if tone_filter != "All":
        filtered_posts = [post for post in filtered_posts if post.tone == tone_filter]
    
    st.write(f"Showing {len(filtered_posts)} of {len(posts)} posts")
    
    # Display posts (demonstrating iteration through objects)
    for post in filtered_posts:
        with st.expander(f"📝 {post.platform} - {post.content_type.title()} ({post.timestamp[:10]})"):
            st.write("**Content:**")
            st.write(post.text)
            
            st.write("**Hashtags:**")
            st.write(" ".join(post.hashtags))
            
            st.write("**Details:**")
            st.write(f"Platform: {post.platform} | Tone: {post.tone} | Type: {post.content_type}")
            
            # Delete button
            if st.button(f"🗑️ Delete", key=f"delete_{post.id}"):
                st.session_state.post_repository.delete_post(post.id)
                st.success("Post deleted!")
                st.rerun()


def settings_page():
    """User settings and preferences page."""
    st.header("Settings & Preferences")

    current_settings = st.session_state.post_repository.load_settings()

    st.subheader("Default Preferences")

    with st.form("settings_form"):
        default_tone = st.selectbox(
            "Default Tone",
            ["professional", "casual", "humorous", "empathetic"],
            index=["professional", "casual", "humorous", "empathetic"].index(current_settings.default_tone)
        )

        default_platforms = st.multiselect(
            "Default Platforms",
            ["Facebook", "Twitter", "Instagram", "LinkedIn"],
            default=current_settings.default_platforms
        )

        api_key = st.text_input(
            "API Key (for OpenRouter free LLM)",
            value=current_settings.api_key,
            type="password",
            help="Get a free API key at https://openrouter.ai/ and paste it here."
        )

        submitted = st.form_submit_button("💾 Save Settings")

        if submitted:
            new_settings = UserSettings(
                default_tone=default_tone,
                default_platforms=default_platforms,
                api_key=api_key
            )
            st.session_state.post_repository.save_settings(new_settings)
            st.session_state.llm_service = LLMService(api_key) if api_key else None
            st.success("Settings saved successfully!")

    st.subheader("Usage Statistics")
    posts = st.session_state.post_repository.get_all_posts()

    if posts:
        platform_counts = {}
        tone_counts = {}
        for post in posts:
            platform_counts[post.platform] = platform_counts.get(post.platform, 0) + 1
            tone_counts[post.tone] = tone_counts.get(post.tone, 0) + 1
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Posts by Platform:**")
            for platform, count in platform_counts.items():
                st.write(f"- {platform}: {count}")
        with col2:
            st.write("**Posts by Tone:**")
            for tone, count in tone_counts.items():
                st.write(f"- {tone.title()}: {count}")
        st.metric("Total Posts Generated", len(posts))
    else:
        st.info("No posts generated yet.")


if __name__ == "__main__":
    main()