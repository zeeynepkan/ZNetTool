# Integrated Network Application

## Project Overview

This project is an integrated network application that combines 5 different network programming modules into a single, cohesive application. The project demonstrates various network programming concepts including socket programming, time synchronization, error handling, and data integration.

## Author
**Zeynep KAN**  
**Project Date:** 2024  
**Project Deadline:** 24.10.2025 23:59

## Project Structure

The project consists of the following components:

### Core Modules (Original - Do Not Modify)
1. **`machine_information_module.py`** - Machine Information Module
2. **`echo_test_module.py`** - Echo Test Module  
3. **`sntp_time_module.py`** - SNTP Time Check Module
4. **`error_settings_module.py`** - Socket Settings & Error Management Module
5. **`simple_chat_module.py`** - Chat Application Module

### Integration Components (New)
6. **`main_integrated_app.py`** - Main integrated application with interactive menu
7. **`data_integration_module.py`** - Data integration and analysis module
8. **`README.md`** - This documentation file

### Generated Files
- **`app_integration_log.txt`** - Application integration log
- **`integration_data.json`** - Persistent integration data
- **`socket_settings_log.txt`** - Socket settings log (from original module)
- **`chat_log.txt`** - Chat application log (from original module)

## Features

### Main Menu System
- Interactive menu allowing users to choose which module to run
- Options: Machine Information, Echo Test, SNTP Time Check, Socket Settings, Chat, and Error Management
- Data Integration Demo showing how modules work together
- Integration log viewer

### Modular Approach
- Each module is designed as a separate Python function or class
- Main program calls the relevant module based on user's choice
- No modifications to original modules - they remain unchanged

### Data Integration
- **Echo Test ↔ Error Management**: Echo test results are analyzed and can be linked with error management
- **SNTP Time Integration**: Time information from SNTP module is used across other modules for logging and time comparison
- **Cross-Module Logging**: All modules share common logging and error handling
- **Data Persistence**: Integration data is stored in JSON format for analysis

## Installation and Setup

### Prerequisites
- Python 3.7 or higher
- Required Python libraries (install via pip):

```bash
pip install psutil
```

### Installation Steps

1. **Clone or download the project files**
2. **Ensure all Python files are in the same directory**
3. **Install required dependencies:**
   ```bash
   pip install psutil
   ```

## Usage

### Running the Integrated Application

```bash
python main_integrated_app.py
```

### Main Menu Options

1. **Machine Information** - Display hostname, IP address, and network interfaces
2. **Echo Test** - Run echo server/client tests with port configuration
3. **SNTP Time Check** - Synchronize with NTP server and compare with local time
4. **Socket Settings & Error Management** - Advanced socket configuration and error handling
5. **Chat Application** - Multi-client chat server/client application
6. **Data Integration Demo** - View how modules integrate and share data
7. **View Integration Log** - Display application integration logs
8. **Exit** - Close the application

### Individual Module Usage

You can still run individual modules directly:

```bash
# Machine Information
python machine_information_module.py

# Echo Test (Server)
python echo_test_module.py --mode server --port 8880

# Echo Test (Client)  
python echo_test_module.py --mode client --port 8880

# SNTP Time Check
python sntp_time_module.py

# Socket Settings (Server)
python error_settings_module.py --mode server --port 5000

# Socket Settings (Client)
python error_settings_module.py --mode client --port 5000 --name client1

# Chat Application
python simple_chat_module.py
```

## Data Integration Features

### Echo Test Integration
- Test results are stored with timestamps
- Response times are measured and analyzed
- Success/failure rates are tracked
- Results can be correlated with error management data

### SNTP Time Integration
- Time synchronization data is stored
- Time differences are calculated and analyzed
- Time data is used for logging across all modules
- Sync quality is assessed (Excellent/Good/Fair/Poor)

### Error Management Integration
- Socket errors are categorized by module
- Error patterns are analyzed
- Error rates are tracked over time
- Integration with echo test results for comprehensive analysis

### Data Analysis Features
- **Echo Test Analysis**: Success rates, response times, failure analysis
- **Time Sync Analysis**: Synchronization quality, time differences
- **Error Analysis**: Error patterns, module-specific error rates
- **Integration Summary**: Overall system health and activity

## File Structure

```
project_directory/
├── machine_information_module.py    # Original module
├── echo_test_module.py             # Original module  
├── sntp_time_module.py             # Original module
├── error_settings_module.py       # Original module
├── simple_chat_module.py          # Original module
├── main_integrated_app.py          # NEW: Main integration app
├── data_integration_module.py      # NEW: Data integration
├── README.md                       # NEW: Documentation
├── app_integration_log.txt         # Generated: App logs
├── integration_data.json           # Generated: Integration data
├── socket_settings_log.txt         # Generated: Socket logs
└── chat_log.txt                    # Generated: Chat logs
```

## Technical Details

### Integration Architecture
- **Modular Design**: Each original module remains unchanged
- **Wrapper Functions**: Integration app wraps original modules
- **Data Flow**: Information flows between modules through integration layer
- **Persistence**: Data is stored in JSON format for analysis

### Error Handling
- Comprehensive error handling across all modules
- Error logging and categorization
- Graceful degradation when modules fail
- User-friendly error messages

### Logging System
- Multi-level logging (INFO, WARNING, ERROR)
- Timestamped log entries
- Module-specific log files
- Integration log for cross-module activities

## Testing

### Test Scenarios

1. **Basic Module Testing**
   - Run each module individually
   - Verify all modules work correctly
   - Check error handling

2. **Integration Testing**
   - Run the integrated application
   - Test menu navigation
   - Verify data integration features

3. **Data Integration Testing**
   - Run echo tests and check data storage
   - Run SNTP checks and verify time data
   - Test error logging and analysis

### Expected Outputs

- **Machine Information**: Hostname, IP, network interfaces
- **Echo Test**: Successful echo communication with response time
- **SNTP Time**: Server time, local time, time difference
- **Socket Settings**: Advanced socket configuration and error handling
- **Chat Application**: Multi-client chat functionality
- **Integration**: Cross-module data sharing and analysis

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   - Change port numbers in module configurations
   - Check for running processes using the same ports

2. **Connection Refused**
   - Ensure server modules are running before clients
   - Check firewall settings

3. **Import Errors**
   - Verify all files are in the same directory
   - Check Python version compatibility

4. **Permission Errors**
   - Run with appropriate permissions for file operations
   - Check directory write permissions

### Debug Mode

Enable debug logging by modifying the integration app:
```python
# In main_integrated_app.py, add debug=True to log_message calls
self.log_message("Debug message", debug=True)
```

## Project Deliverables

✅ **Code Files**: All Python files including libraries  
✅ **Documentation**: Comments within code and README file  
✅ **Execution Guide**: Instructions for running the project  
✅ **Test Outputs**: Screen outputs and log files demonstrating functionality  

## Future Enhancements

- Real-time data visualization
- Advanced error pattern recognition
- Network performance monitoring
- Automated testing suite
- Web-based interface
- Database integration for large-scale data

## License

This project is created for educational purposes as part of a network programming course.

## Contact

For questions or issues related to this project, please contact the author.

---

**Note**: This project maintains the original modules unchanged while adding integration capabilities. All original functionality is preserved while providing enhanced data integration and analysis features.
