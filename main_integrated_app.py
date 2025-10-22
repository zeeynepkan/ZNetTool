#!/usr/bin/env python3
"""
Integrated Network Application
==============================

This is the main integration application that combines all 5 modules:
1. Machine Information Module
2. Echo Test Module  
3. SNTP Time Check Module
4. Socket Settings Module (Error Management)
5. Chat Module

Author: Zeynep KAN
Project: Network Programming Integration
Date: 2024
"""

import os
import sys
import subprocess
import time
import threading
from datetime import datetime

# Import all modules
from machine_information_module import print_machine_info
from echo_test_module import echo_server, echo_client
from sntp_time_module import sntp_client
from error_settings_module import ChatServer, ChatClient
from simple_chat_module import run_server as chat_server, run_client as chat_client

class IntegratedNetworkApp:
    """
    Main integrated application class that manages all modules
    """
    
    def __init__(self):
        self.app_name = "Integrated Network Application"
        self.version = "1.0.0"
        self.log_file = "app_integration_log.txt"
        self.echo_test_results = []
        self.sntp_time_data = {}
        
    def log_message(self, message):
        """Log messages to both console and file"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        print(log_entry)
        
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")
    
    def display_banner(self):
        """Display application banner"""
        print("=" * 60)
        print(f"    {self.app_name} v{self.version}")
        print("=" * 60)
        print("    Network Programming Integration Project")
        print("    Author: Zeynep KAN")
        print("    Date: 2024")
        print("=" * 60)
        print()
    
    def display_main_menu(self):
        """Display the main interactive menu"""
        print("\n" + "=" * 40)
        print("    MAIN MENU - Select Module")
        print("=" * 40)
        print("1. Machine Information")
        print("2. Echo Test")
        print("3. SNTP Time Check")
        print("4. Socket Settings & Error Management")
        print("5. Chat Application")
        print("6. Data Integration Demo")
        print("7. View Integration Log")
        print("8. Exit")
        print("=" * 40)
    
    def run_machine_info(self):
        """Run Machine Information Module"""
        self.log_message("Starting Machine Information Module...")
        print("\n" + "=" * 50)
        print("    MACHINE INFORMATION MODULE")
        print("=" * 50)
        
        try:
            print_machine_info()
            self.log_message("Machine Information Module completed successfully")
        except Exception as e:
            error_msg = f"Machine Information Module failed: {e}"
            print(f"❌ {error_msg}")
            self.log_message(error_msg)
        
        input("\nPress Enter to continue...")
    
    def run_echo_test(self):
        """Run Echo Test Module with integration"""
        self.log_message("Starting Echo Test Module...")
        print("\n" + "=" * 50)
        print("    ECHO TEST MODULE")
        print("=" * 50)
        
        print("Echo Test Options:")
        print("1. Run as Server")
        print("2. Run as Client")
        print("3. Run Both (Server in background)")
        
        choice = input("Select option (1-3): ").strip()
        
        try:
            if choice == "1":
                port = int(input("Enter port number (default 8880): ") or "8880")
                print(f"Starting Echo Server on port {port}...")
                print("Press Ctrl+C to stop the server")
                echo_server(port)
                
            elif choice == "2":
                port = int(input("Enter server port (default 8880): ") or "8880")
                print(f"Connecting to Echo Server on port {port}...")
                echo_client(port)
                
                # Store results for integration
                self.echo_test_results.append({
                    'timestamp': datetime.now().isoformat(),
                    'port': port,
                    'status': 'completed'
                })
                
            elif choice == "3":
                port = int(input("Enter port number (default 8880): ") or "8880")
                
                # Start server in background thread
                server_thread = threading.Thread(target=echo_server, args=(port,), daemon=True)
                server_thread.start()
                
                print(f"Echo Server started in background on port {port}")
                time.sleep(2)  # Wait for server to start
                
                # Run client
                print("Running Echo Client...")
                echo_client(port)
                
                # Store results for integration
                self.echo_test_results.append({
                    'timestamp': datetime.now().isoformat(),
                    'port': port,
                    'status': 'completed'
                })
                
            else:
                print("Invalid choice!")
                return
                
            self.log_message("Echo Test Module completed successfully")
            
        except Exception as e:
            error_msg = f"Echo Test Module failed: {e}"
            print(f"❌ {error_msg}")
            self.log_message(error_msg)
        
        input("\nPress Enter to continue...")
    
    def run_sntp_time(self):
        """Run SNTP Time Check Module"""
        self.log_message("Starting SNTP Time Check Module...")
        print("\n" + "=" * 50)
        print("    SNTP TIME CHECK MODULE")
        print("=" * 50)
        
        try:
            sntp_client()
            
            # Store time data for integration
            self.sntp_time_data = {
                'timestamp': datetime.now().isoformat(),
                'status': 'completed'
            }
            
            self.log_message("SNTP Time Check Module completed successfully")
            
        except Exception as e:
            error_msg = f"SNTP Time Check Module failed: {e}"
            print(f"❌ {error_msg}")
            self.log_message(error_msg)
        
        input("\nPress Enter to continue...")
    
    def run_socket_settings(self):
        """Run Socket Settings & Error Management Module"""
        self.log_message("Starting Socket Settings & Error Management Module...")
        print("\n" + "=" * 50)
        print("    SOCKET SETTINGS & ERROR MANAGEMENT")
        print("=" * 50)
        
        print("Socket Settings Options:")
        print("1. Run as Server")
        print("2. Run as Client")
        
        choice = input("Select option (1-2): ").strip()
        
        try:
            if choice == "1":
                port = int(input("Enter port number (default 5000): ") or "5000")
                timeout = float(input("Enter timeout in seconds (default 5.0): ") or "5.0")
                nonblock = input("Use non-blocking mode? (y/n): ").lower() == 'y'
                
                print(f"Starting Socket Settings Server on port {port}...")
                print("Press Ctrl+C to stop the server")
                
                server = ChatServer(port, timeout=timeout, blocking=not nonblock)
                server.run()
                
            elif choice == "2":
                port = int(input("Enter server port (default 5000): ") or "5000")
                name = input("Enter client name (default client1): ") or "client1"
                timeout = float(input("Enter timeout in seconds (default 3.0): ") or "3.0")
                nonblock = input("Use non-blocking mode? (y/n): ").lower() == 'y'
                
                print(f"Connecting to Socket Settings Server on port {port}...")
                print("Type messages and press Enter. Press Ctrl+C to exit.")
                
                client = ChatClient(name, port, timeout=timeout, blocking=not nonblock)
                client.run()
                
            else:
                print("Invalid choice!")
                return
                
            self.log_message("Socket Settings & Error Management Module completed successfully")
            
        except Exception as e:
            error_msg = f"Socket Settings Module failed: {e}"
            print(f"❌ {error_msg}")
            self.log_message(error_msg)
        
        input("\nPress Enter to continue...")
    
    def run_chat_application(self):
        """Run Chat Application Module"""
        self.log_message("Starting Chat Application Module...")
        print("\n" + "=" * 50)
        print("    CHAT APPLICATION MODULE")
        print("=" * 50)
        
        print("Chat Application Options:")
        print("1. Run as Server")
        print("2. Run as Client")
        
        choice = input("Select option (1-2): ").strip()
        
        try:
            if choice == "1":
                print("Starting Chat Server...")
                print("Press Ctrl+C to stop the server")
                chat_server()
                
            elif choice == "2":
                print("Starting Chat Client...")
                print("Type messages and press Enter. Type 'exit' or 'quit' to exit.")
                chat_client()
                
            else:
                print("Invalid choice!")
                return
                
            self.log_message("Chat Application Module completed successfully")
            
        except Exception as e:
            error_msg = f"Chat Application Module failed: {e}"
            print(f"❌ {error_msg}")
            self.log_message(error_msg)
        
        input("\nPress Enter to continue...")
    
    def run_data_integration_demo(self):
        """Demonstrate data integration between modules"""
        self.log_message("Starting Data Integration Demo...")
        print("\n" + "=" * 50)
        print("    DATA INTEGRATION DEMO")
        print("=" * 50)
        
        print("This demo shows how data from different modules can be integrated:")
        print()
        
        # Show SNTP time integration
        if self.sntp_time_data:
            print("🕐 SNTP Time Data Integration:")
            print(f"   Last SNTP check: {self.sntp_time_data.get('timestamp', 'N/A')}")
            print(f"   Status: {self.sntp_time_data.get('status', 'N/A')}")
        else:
            print("🕐 SNTP Time Data: No data available (run SNTP module first)")
        
        print()
        
        # Show Echo Test results integration
        if self.echo_test_results:
            print("📡 Echo Test Results Integration:")
            for i, result in enumerate(self.echo_test_results, 1):
                print(f"   Test {i}: Port {result.get('port', 'N/A')} - {result.get('status', 'N/A')}")
                print(f"   Timestamp: {result.get('timestamp', 'N/A')}")
        else:
            print("📡 Echo Test Results: No data available (run Echo Test module first)")
        
        print()
        
        # Show integration possibilities
        print("🔗 Integration Possibilities:")
        print("   • SNTP time can be used for logging timestamps in all modules")
        print("   • Echo Test results can be analyzed by Error Management module")
        print("   • Machine Information can be logged with timestamps")
        print("   • All modules can share common logging and error handling")
        
        self.log_message("Data Integration Demo completed")
        input("\nPress Enter to continue...")
    
    def view_integration_log(self):
        """View the integration log file"""
        print("\n" + "=" * 50)
        print("    INTEGRATION LOG")
        print("=" * 50)
        
        try:
            if os.path.exists(self.log_file):
                with open(self.log_file, "r", encoding="utf-8") as f:
                    log_content = f.read()
                    if log_content.strip():
                        print(log_content)
                    else:
                        print("Log file is empty.")
            else:
                print("No log file found.")
        except Exception as e:
            print(f"Error reading log file: {e}")
        
        input("\nPress Enter to continue...")
    
    def run(self):
        """Main application loop"""
        self.display_banner()
        self.log_message("Integrated Network Application started")
        
        while True:
            self.display_main_menu()
            
            try:
                choice = input("Enter your choice (1-8): ").strip()
                
                if choice == "1":
                    self.run_machine_info()
                elif choice == "2":
                    self.run_echo_test()
                elif choice == "3":
                    self.run_sntp_time()
                elif choice == "4":
                    self.run_socket_settings()
                elif choice == "5":
                    self.run_chat_application()
                elif choice == "6":
                    self.run_data_integration_demo()
                elif choice == "7":
                    self.view_integration_log()
                elif choice == "8":
                    print("\n👋 Thank you for using the Integrated Network Application!")
                    self.log_message("Application closed by user")
                    break
                else:
                    print("❌ Invalid choice! Please enter a number between 1-8.")
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                print("\n\n👋 Application interrupted by user.")
                self.log_message("Application interrupted by user")
                break
            except Exception as e:
                print(f"\n❌ Unexpected error: {e}")
                self.log_message(f"Unexpected error: {e}")
                time.sleep(2)

def main():
    """Main entry point"""
    try:
        app = IntegratedNetworkApp()
        app.run()
    except Exception as e:
        print(f"Failed to start application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
