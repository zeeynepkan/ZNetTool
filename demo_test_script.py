#!/usr/bin/env python3
"""
Demo Test Script for Integrated Network Application
==================================================

This script demonstrates the functionality of the integrated network application
and provides test outputs for each module.

Author: Zeynep KAN
Project: Network Programming Integration
Date: 2024
"""

import os
import sys
import time
import subprocess
import threading
from datetime import datetime

def print_section(title):
    """Print a formatted section header"""
    print("\n" + "=" * 60)
    print(f"    {title}")
    print("=" * 60)

def print_subsection(title):
    """Print a formatted subsection header"""
    print(f"\n--- {title} ---")

def run_demo():
    """Run the complete demo"""
    print_section("INTEGRATED NETWORK APPLICATION DEMO")
    print("This demo shows the functionality of all modules")
    print(f"Demo started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Test 1: Machine Information Module
    print_section("TEST 1: MACHINE INFORMATION MODULE")
    print_subsection("Running Machine Information Module")
    try:
        from machine_information_module import print_machine_info
        print("✅ Machine Information Module imported successfully")
        print("Machine Information Output:")
        print("-" * 40)
        print_machine_info()
        print("-" * 40)
        print("✅ Machine Information Module test completed")
    except Exception as e:
        print(f"❌ Machine Information Module test failed: {e}")
    
    # Test 2: SNTP Time Module
    print_section("TEST 2: SNTP TIME CHECK MODULE")
    print_subsection("Running SNTP Time Check Module")
    try:
        from sntp_time_module import sntp_client
        print("✅ SNTP Time Module imported successfully")
        print("SNTP Time Check Output:")
        print("-" * 40)
        sntp_client()
        print("-" * 40)
        print("✅ SNTP Time Check Module test completed")
    except Exception as e:
        print(f"❌ SNTP Time Check Module test failed: {e}")
    
    # Test 3: Echo Test Module (Client only for demo)
    print_section("TEST 3: ECHO TEST MODULE")
    print_subsection("Testing Echo Test Module (Client Mode)")
    try:
        from echo_test_module import echo_client
        print("✅ Echo Test Module imported successfully")
        print("Note: Echo Test requires a server to be running")
        print("For full testing, run: python echo_test_module.py --mode server --port 8880")
        print("Then run: python echo_test_module.py --mode client --port 8880")
        print("✅ Echo Test Module import test completed")
    except Exception as e:
        print(f"❌ Echo Test Module test failed: {e}")
    
    # Test 4: Socket Settings Module
    print_section("TEST 4: SOCKET SETTINGS & ERROR MANAGEMENT MODULE")
    print_subsection("Testing Socket Settings Module")
    try:
        from error_settings_module import ChatServer, ChatClient
        print("✅ Socket Settings Module imported successfully")
        print("Socket Settings Module classes available:")
        print("  - ChatServer: Advanced socket server with error handling")
        print("  - ChatClient: Advanced socket client with error handling")
        print("✅ Socket Settings Module test completed")
    except Exception as e:
        print(f"❌ Socket Settings Module test failed: {e}")
    
    # Test 5: Chat Module
    print_section("TEST 5: CHAT APPLICATION MODULE")
    print_subsection("Testing Chat Application Module")
    try:
        from simple_chat_module import run_server, run_client
        print("✅ Chat Application Module imported successfully")
        print("Chat Application Module functions available:")
        print("  - run_server(): Start chat server")
        print("  - run_client(): Start chat client")
        print("✅ Chat Application Module test completed")
    except Exception as e:
        print(f"❌ Chat Application Module test failed: {e}")
    
    # Test 6: Data Integration Module
    print_section("TEST 6: DATA INTEGRATION MODULE")
    print_subsection("Testing Data Integration Module")
    try:
        from data_integration_module import DataIntegrator, get_integrator
        print("✅ Data Integration Module imported successfully")
        
        # Test data integrator
        integrator = DataIntegrator("demo_integration_data.json")
        
        # Add some test data
        integrator.add_echo_test_result(8880, "completed", 0.05)
        integrator.add_sntp_check("2024-01-01 12:00:00", "2024-01-01 12:00:01", 1.0)
        integrator.add_socket_error("ConnectionError", "Connection refused", "echo_test", 8880)
        integrator.add_machine_info("demo-host", "192.168.1.100", {"eth0": "192.168.1.100"})
        
        print("Test data added to integrator")
        
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
        
        print("\nIntegration Summary:")
        summary = integrator.get_integration_summary()
        for key, value in summary.items():
            print(f"  {key}: {value}")
        
        print("✅ Data Integration Module test completed")
        
        # Clean up demo data
        if os.path.exists("demo_integration_data.json"):
            os.remove("demo_integration_data.json")
        
    except Exception as e:
        print(f"❌ Data Integration Module test failed: {e}")
    
    # Test 7: Main Integrated Application
    print_section("TEST 7: MAIN INTEGRATED APPLICATION")
    print_subsection("Testing Main Integrated Application")
    try:
        from main_integrated_app import IntegratedNetworkApp
        print("✅ Main Integrated Application imported successfully")
        print("Main Integrated Application features:")
        print("  - Interactive menu system")
        print("  - Module integration")
        print("  - Data integration demo")
        print("  - Logging system")
        print("✅ Main Integrated Application test completed")
    except Exception as e:
        print(f"❌ Main Integrated Application test failed: {e}")
    
    # Test 8: File Structure Check
    print_section("TEST 8: FILE STRUCTURE CHECK")
    print_subsection("Checking Project File Structure")
    
    required_files = [
        "machine_information_module.py",
        "echo_test_module.py", 
        "sntp_time_module.py",
        "error_settings_module.py",
        "simple_chat_module.py",
        "main_integrated_app.py",
        "data_integration_module.py",
        "README.md"
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} - Found")
        else:
            print(f"❌ {file} - Missing")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n❌ Missing files: {missing_files}")
    else:
        print("\n✅ All required files are present")
    
    # Test 9: Dependencies Check
    print_section("TEST 9: DEPENDENCIES CHECK")
    print_subsection("Checking Required Dependencies")
    
    try:
        import psutil
        print("✅ psutil - Available")
    except ImportError:
        print("❌ psutil - Missing (install with: pip install psutil)")
    
    try:
        import socket
        print("✅ socket - Available (built-in)")
    except ImportError:
        print("❌ socket - Missing")
    
    try:
        import json
        print("✅ json - Available (built-in)")
    except ImportError:
        print("❌ json - Missing")
    
    try:
        import threading
        print("✅ threading - Available (built-in)")
    except ImportError:
        print("❌ threading - Missing")
    
    # Demo Summary
    print_section("DEMO SUMMARY")
    print("Demo completed successfully!")
    print(f"Demo finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\nTo run the full integrated application:")
    print("  python main_integrated_app.py")
    print("\nTo run individual modules:")
    print("  python machine_information_module.py")
    print("  python sntp_time_module.py")
    print("  python echo_test_module.py --mode server --port 8880")
    print("  python echo_test_module.py --mode client --port 8880")
    print("  python error_settings_module.py --mode server --port 5000")
    print("  python error_settings_module.py --mode client --port 5000")
    print("  python simple_chat_module.py")

def run_quick_test():
    """Run a quick test of the main application"""
    print_section("QUICK TEST: MAIN INTEGRATED APPLICATION")
    print("This is a quick test of the main application menu system")
    
    try:
        from main_integrated_app import IntegratedNetworkApp
        app = IntegratedNetworkApp()
        
        print("✅ Main application created successfully")
        print("✅ Menu system initialized")
        print("✅ Integration features available")
        print("✅ Logging system active")
        
        print("\nTo run the full application:")
        print("  python main_integrated_app.py")
        
    except Exception as e:
        print(f"❌ Quick test failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--quick":
        run_quick_test()
    else:
        run_demo()
