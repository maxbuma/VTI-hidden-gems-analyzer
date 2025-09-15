# VTI Hidden Gems Analyzer - Email Configuration Template
# Copy this file to vti_config.py and add your credentials

# Gmail Setup Instructions:
# 1. Enable 2-factor authentication on your Google account
# 2. Go to Google Account → Security → App passwords
# 3. Generate an app password for "Mail"
# 4. Use that app password below (not your regular Gmail password)

EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-16-character-app-password"

# Example:
# EMAIL_ADDRESS = "john.doe@gmail.com"
# EMAIL_PASSWORD = "abcd efgh ijkl mnop"

# Portfolio Configuration (Optional)
PORTFOLIO_SIZE = 5000  # Test portfolio size in dollars
MAX_POSITION_SIZE = 500  # Maximum per stock (10% of portfolio)
HIDDEN_GEMS_ALLOCATION = 0.30  # 30% allocation to hidden gems

# Analysis Configuration (Optional)
PREMIUM_THRESHOLD = 15    # Premium gems minimum score
QUALITY_THRESHOLD = 10    # Quality gems minimum score
MIN_MARKET_CAP = 500e6    # $500M minimum market cap
MAX_MARKET_CAP = 50e9     # $50B maximum market cap