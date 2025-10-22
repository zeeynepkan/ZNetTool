#!/usr/bin/env python3
"""
Usage Examples for Integrated Network Application
=================================================

This script provides practical examples of how to use the integrated
network application and its individual modules.

Author: Zeynep KAN
Project: Network Programming Integration
Date: 2024
"""

import os
import sys
import time
import threading
from datetime import datetime

def example_1_machine_info():
    """Example 1: Machine Information Module"""
    print("=" * 50)
    print("EXAMPLE 1: Machine Information Module")
    print("=" * 50)
    
    try:
        from machine_information_module import print_machine_info
        print("Getting machine information...")
        print_machine_info()
    except Exception as e:
        print(f"Error: {e}")

def example_2_sntp_time():
    """Example 2: SNTP Time Check Module"""
    print("=" * 50)
    print("EXAMPLE 2: SNTP Time Check Module")
    print("=" * 50)
    
    try:
        from sntp_time_module import sntp_client
        print("Checking time synchronization...")
        sntp_client()
    except Exception as e:
        print(f"Error: {e}")

def example_3_echo_test():
    """Example 3: Echo Test Module"""
    print("=" * 50)
    print("EXAMPLE 3: Echo Test Module")
    print("=" * 50)
    
    print("Echo Test Module Usage Examples:")
    print("1. Start Echo Server:")
    print("   python echo_test_module.py --mode server --port 8880")
    print("2. Connect Echo Client:")
    print("   python echo_test_module.py --mode client --port 8880")
    print("3. Custom Port:")
    print("   python echo_test_module.py --mode server --port 9999")
    print("   python echo_test_module.py --mode client --port 9999")

def example_4_socket_settings():
    """Example 4: Socket Settings & Error Management"""
    print("=" * 50)
    print("EXAMPLE 4: Socket Settings & Error Management")
    print("=" * 50)
    
    print("Socket Settings Module Usage Examples:")
    print("1. Start Server with default settings:")
    print("   python error_settings_module.py --mode server --port 5000")
    print("2. Connect Client:")
    print("   python error_settings_module.py --mode client --port 5000 --name client1")
    print("3. Advanced settings:")
    print("   python error_settings_module.py --mode server --port 5000 --timeout 10 --nonblock")
    print("   python error_settings_module.py --mode client --port 5000 --timeout 5 --nonblock")

def example_5_chat_application():
    """Example 5: Chat Application Module"""
    print("=" * 50)
    print("EXAMPLE 5: Chat Application Module")
    print("=" * 50)
    
    print("Chat Application Module Usage Examples:")
    print("1. Start Chat Server:")
    print("   python simple_chat_module.py")
    print("   (Then select 's' for server)")
    print("2. Connect Chat Client:")
    print("   python simple_chat_module.py")
    print("   (Then select 'c' for client)")

def example_6_data_integration():
    """Example 6: Data Integration Module"""
    print("=" * 50)
    print("EXAMPLE 6: Data Integration Module")
    print("=" * 50)
    
    try:
        from data_integration_module import DataIntegrator
        
        # Create integrator
        integrator = DataIntegrator("example_integration_data.json")
        
        # Add some example data
        print("Adding example data...")
        integrator.add_echo_test_result(8880, "completed", 0.05)
        integrator.add_sntp_check("2024-01-01 12:00:00", "2024-01-01 12:00:01", 1.0)
        integrator.add_socket_error("ConnectionError", "Connection refused", "echo_test", 8880)
        integrator.add_machine_info("example-host", "192.168.1.100", {"eth0": "192.168.1.100"})
        
        # Show analysis
        print("\nEcho Test Analysis:")
        echo_analysis = integrator.get_echo_test_analysis()
        for key, value in echo_analysis.items():
            print(f"  {key}: {value}")
        
        print("\nTime Sync Analysis:")
        time_analysis = integrator.get_time_sync_analysis()
        for key, value in time_analysis.items():
            print(f"  {key}: {value}")
        
        print("\nError Analysis:")
        error_analysis = integrator.get_error_analysis()
        for key, value in error_analysis.items():
            print(f"  {key}: {value}")
        
        # Clean up
        if os.path.exists("example_integration_data.json"):
            os.remove("example_integration_data.json")
        
    except Exception as e:
        print(f"Error: {e}")

def example_7_integrated_app():
    """Example 7: Main Integrated Application"""
    print("=" * 50)
    print("EXAMPLE 7: Main Integrated Application")
    print("=" * 50)
    
    print("Main Integrated Application Usage:")
    print("1. Run the integrated application:")
    print("   python main_integrated_app.py")
    print("2. Use the interactive menu to:")
    print("   - Select modules to run")
    print("   - View data integration")
    print("   - Check integration logs")
    print("   - Exit the application")

def example_8_advanced_usage():
    """Example 8: Advanced Usage Scenarios"""
    print("=" * 50)
    print("EXAMPLE 8: Advanced Usage Scenarios")
    print("=" * 50)
    
    print("Advanced Usage Scenarios:")
    print("1. Network Testing:")
    print("   - Run echo tests on different ports")
    print("   - Monitor network performance")
    print("   - Analyze connection errors")
    
    print("\n2. Time Synchronization:")
    print("   - Check time accuracy")
    print("   - Monitor time drift")
    print("   - Log time differences")
    
    print("\n3. Error Management:")
    print("   - Track socket errors")
    print("   - Analyze error patterns")
    print("   - Monitor system health")
    
    print("\n4. Data Integration:")
    print("   - Correlate test results")
    print("   - Analyze performance trends")
    print("   - Generate reports")

def example_9_troubleshooting():
    """Example 9: Troubleshooting Common Issues"""
    print("=" * 50)
    print("EXAMPLE 9: Troubleshooting Common Issues")
    print("=" * 50)
    
    print("Common Issues and Solutions:")
    print("1. Port Already in Use:")
    print("   - Check running processes: netstat -an | findstr :8880")
    print("   - Use different port numbers")
    print("   - Kill existing processes if needed")
    
    print("\n2. Connection Refused:")
    print("   - Ensure server is running before client")
    print("   - Check firewall settings")
    print("   - Verify port numbers match")
    
    print("\n3. Import Errors:")
    print("   - Verify all files are in the same directory")
    print("   - Check Python version compatibility")
    print("   - Install required dependencies: pip install psutil")
    
    print("\n4. Permission Errors:")
    print("   - Run with appropriate permissions")
    print("   - Check directory write permissions")
    print("   - Verify file access rights")

def example_10_best_practices():
    """Example 10: Best Practices"""
    print("=" * 50)
    print("EXAMPLE 10: Best Practices")
    print("=" * 50)
    
    print("Best Practices for Using the Application:")
    print("1. Module Testing:")
    print("   - Test each module individually first")
    print("   - Verify all dependencies are installed")
    print("   - Check for port conflicts")
    
    print("\n2. Integration Testing:")
    print("   - Run the integrated application")
    print("   - Test all menu options")
    print("   - Verify data integration features")
    
    print("\n3. Error Handling:")
    print("   - Monitor error logs")
    print("   - Check integration data")
    print("   - Verify system health")
    
    print("\n4. Performance Monitoring:")
    print("   - Track response times")
    print("   - Monitor error rates")
    print("   - Analyze system performance")

def run_all_examples():
    """Run all examples"""
    print("INTEGRATED NETWORK APPLICATION - USAGE EXAMPLES")
    print("=" * 60)
    print(f"Examples started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    examples = [
        example_1_machine_info,
        example_2_sntp_time,
        example_3_echo_test,
        example_4_socket_settings,
        example_5_chat_application,
        example_6_data_integration,
        example_7_integrated_app,
        example_8_advanced_usage,
        example_9_troubleshooting,
        example_10_best_practices
    ]
    
    for i, example in enumerate(examples, 1):
        try:
            example()
            print(f"\n✅ Example {i} completed successfully")
        except Exception as e:
            print(f"\n❌ Example {i} failed: {e}")
        
        if i < len(examples):
            input("\nPress Enter to continue to next example...")
    
    print("\n" + "=" * 60)
    print("ALL EXAMPLES COMPLETED")
    print("=" * 60)
    print(f"Examples finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--help":
            print("Usage Examples for Integrated Network Application")
            print("=" * 50)
            print("python usage_examples.py           # Run all examples")
            print("python usage_examples.py --help    # Show this help")
        else:
            print("Unknown option. Use --help for usage information.")
    else:
        run_all_examples()
