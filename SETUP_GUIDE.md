# 🚀 VTI Hidden Gems Analyzer - Complete Setup Guide

## 📋 **Prerequisites**

### **System Requirements**
- **Python 3.8+** (Python 3.11 recommended)
- **Windows 10/11** (or macOS/Linux)
- **Internet connection** for stock data
- **Gmail account** for email alerts

### **Python Installation (if needed)**
1. Download from [python.org](https://python.org/downloads/)
2. **IMPORTANT**: Check "Add Python to PATH" during installation
3. Restart computer after installation
4. Test: Open Command Prompt, type `python --version`

## ⚙️ **Installation Steps**

### **Step 1: Download the Project**
```bash
# Option A: Git clone (if you have Git)
git clone https://github.com/yourusername/vti-hidden-gems-analyzer.git
cd vti-hidden-gems-analyzer

# Option B: Download ZIP
# Download ZIP from GitHub → Extract to desired folder
```

### **Step 2: Install Python Libraries**
```bash
# Open Command Prompt in project folder
pip install -r vti_requirements.txt

# Or install individually:
pip install yfinance pandas numpy yagmail requests
```

### **Step 3: Configure Email**
1. **Copy template**: `vti_config_template.py` → `vti_config.py`
2. **Edit `vti_config.py`** with your credentials:
```python
EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"  # NOT your regular password!
```

### **Step 4: Gmail App Password Setup**
1. **Enable 2FA**: Google Account → Security → 2-Step Verification
2. **Generate App Password**: Security → App passwords → Select "Mail"
3. **Copy 16-character password**: Use this in `EMAIL_PASSWORD`
4. **Test**: The analyzer will test email sending on first run

## 🎯 **Running the Analyzer**

### **Method 1: IDLE (Recommended for Windows)**
1. **Right-click** `vti_hidden_gems_analyzer.py`
2. **Select** "Edit with IDLE"
3. **Press F5** to run
4. **View results** in the Python shell

### **Method 2: Command Line**
```bash
# Navigate to project folder
cd path/to/vti-hidden-gems-analyzer

# Run analyzer
python vti_hidden_gems_analyzer.py
```

### **Method 3: Double-Click (if configured)**
- **Double-click** the Python file
- **Results appear** in terminal window
- **Window may close quickly** - use IDLE for better experience

## 📊 **What to Expect**

### **Analysis Process**
```
💎 VTI HIDDEN GEMS ANALYZER
📊 Analyzing 60 potential hidden gems...

[  1/60] DXCM  - DexCom Inc.                     💎 SCORE: 18
[  2/60] POOL  - Pool Corporation                💎 SCORE: 16
[  3/60] VEEV  - Veeva Systems Inc.              💎 SCORE: 15
...
[60/60] XYL   - Xylem Inc.                       ⚪ Score: 5

💎 HIDDEN GEMS ANALYSIS COMPLETE
⏱️  Analysis time: 45.2 seconds
🔍 Stocks analyzed: 60
💎 Gems found: 12
🏆 Premium gems: 5
📧 Email sent with top discoveries
```

### **Email Report**
You'll receive a comprehensive email with:
- **Top 10 opportunities** ranked by score
- **Detailed analysis** for each stock
- **Entry points** and risk levels
- **Market cap and ownership** data

## 🔧 **Troubleshooting**

### **Common Issues**

#### **"Python not recognized"**
- **Solution**: Reinstall Python with "Add to PATH" checked
- **Alternative**: Use full path: `C:\Python311\python.exe`

#### **"Module not found"**
- **Solution**: Install requirements: `pip install -r vti_requirements.txt`
- **Check**: Make sure you're in the right directory

#### **"Email authentication failed"**
- **Solution**: Use Gmail app password, not regular password
- **Check**: 2-factor authentication must be enabled
- **Verify**: Test with a simple email first

#### **"No data available"**
- **Solution**: Check internet connection
- **Alternative**: Try running at different times
- **Note**: Some stocks may be delisted or have data issues

#### **"DataFrame truth value error"**
- **Solution**: This is fixed in the latest version
- **Alternative**: Use the simple version if issues persist

### **Performance Issues**

#### **Slow Analysis**
- **Normal**: 60 stocks take 30-60 seconds
- **Optimization**: Run during off-peak hours
- **Alternative**: Reduce stock list for faster analysis

#### **Memory Issues**
- **Solution**: Close other programs while running
- **Alternative**: Analyze in smaller batches
- **Upgrade**: Consider more RAM if persistent

## 📈 **Optimization Tips**

### **Best Times to Run**
- **Market hours**: 9:35 AM - 4:00 PM EST (fresh data)
- **After hours**: 6:00 PM - 8:00 PM EST (less API congestion)
- **Weekends**: Uses last trading day data (still valuable)

### **Customization Options**
- **Adjust scoring**: Modify point values in analyzer
- **Change stock universe**: Edit `get_vti_holdings()` function
- **Email frequency**: Run manually or set up scheduled tasks
- **Portfolio size**: Update config for different account sizes

### **Advanced Usage**
- **Batch analysis**: Run multiple times per day
- **Sector focus**: Analyze specific sectors only
- **Backtesting**: Track historical performance
- **Integration**: Combine with other analysis tools

## 🎯 **Success Checklist**

### **Initial Setup** ✅
- [ ] Python installed and working
- [ ] Libraries installed (`pip install -r vti_requirements.txt`)
- [ ] Email configured (`vti_config.py` with app password)
- [ ] Test run successful (analyzer completes without errors)
- [ ] Email received with results

### **First Week** ✅
- [ ] Run analyzer 2-3 times to understand results
- [ ] Identify 3-5 potential positions
- [ ] Set up tracking spreadsheet
- [ ] Plan position sizes and entry points

### **First Month** ✅
- [ ] Execute 2-4 positions based on signals
- [ ] Set stop losses and profit targets
- [ ] Track performance vs benchmarks
- [ ] Refine strategy based on results

---

**You're now ready to discover hidden gems with professional-grade analysis!** 💎🚀

For support or questions, please open an issue on GitHub or refer to the troubleshooting section above.