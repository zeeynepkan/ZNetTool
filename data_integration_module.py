#!/usr/bin/env python3
"""
Data Integration Module
=======================

This module provides data integration capabilities between different modules:
- Echo Test results integration with Error Management
- SNTP time data sharing across modules
- Common logging and error handling
- Data persistence and analysis

Author: Zeynep KAN
Project: Network Programming Integration
Date: 2024
"""

import json
import os
import time
from datetime import datetime
from typing import Dict, List, Any, Optional

class DataIntegrator:
    """
    Handles data integration between different modules
    """
    
    def __init__(self, data_file: str = "integration_data.json"):
        self.data_file = data_file
        self.data = self.load_data()
    
    def load_data(self) -> Dict[str, Any]:
        """Load existing integration data from file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Could not load integration data: {e}")
        
        return {
            'echo_tests': [],
            'sntp_checks': [],
            'machine_info': [],
            'socket_errors': [],
            'chat_sessions': [],
            'integration_log': []
        }
    
    def save_data(self):
        """Save integration data to file"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"Error saving integration data: {e}")
    
    def add_echo_test_result(self, port: int, status: str, response_time: Optional[float] = None, 
                            error_message: Optional[str] = None):
        """Add echo test result to integration data"""
        result = {
            'timestamp': datetime.now().isoformat(),
            'port': port,
            'status': status,
            'response_time': response_time,
            'error_message': error_message
        }
        
        self.data['echo_tests'].append(result)
        self.log_integration('echo_test', f"Echo test on port {port}: {status}")
        self.save_data()
    
    def add_sntp_check(self, server_time: str, local_time: str, time_difference: float, 
                      server: str = "pool.ntp.org"):
        """Add SNTP time check result to integration data"""
        result = {
            'timestamp': datetime.now().isoformat(),
            'server': server,
            'server_time': server_time,
            'local_time': local_time,
            'time_difference': time_difference
        }
        
        self.data['sntp_checks'].append(result)
        self.log_integration('sntp_check', f"SNTP check: {time_difference:.2f}s difference")
        self.save_data()
    
    def add_machine_info(self, hostname: str, ip_address: str, network_interfaces: Dict):
        """Add machine information to integration data"""
        result = {
            'timestamp': datetime.now().isoformat(),
            'hostname': hostname,
            'ip_address': ip_address,
            'network_interfaces': network_interfaces
        }
        
        self.data['machine_info'].append(result)
        self.log_integration('machine_info', f"Machine info collected for {hostname}")
        self.save_data()
    
    def add_socket_error(self, error_type: str, error_message: str, module: str, 
                        port: Optional[int] = None):
        """Add socket error to integration data"""
        result = {
            'timestamp': datetime.now().isoformat(),
            'error_type': error_type,
            'error_message': error_message,
            'module': module,
            'port': port
        }
        
        self.data['socket_errors'].append(result)
        self.log_integration('socket_error', f"Socket error in {module}: {error_type}")
        self.save_data()
    
    def add_chat_session(self, session_type: str, port: int, duration: Optional[float] = None,
                        message_count: Optional[int] = None):
        """Add chat session information to integration data"""
        result = {
            'timestamp': datetime.now().isoformat(),
            'session_type': session_type,
            'port': port,
            'duration': duration,
            'message_count': message_count
        }
        
        self.data['chat_sessions'].append(result)
        self.log_integration('chat_session', f"Chat session: {session_type} on port {port}")
        self.save_data()
    
    def log_integration(self, module: str, message: str):
        """Log integration events"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'module': module,
            'message': message
        }
        
        self.data['integration_log'].append(log_entry)
    
    def get_echo_test_analysis(self) -> Dict[str, Any]:
        """Analyze echo test results"""
        if not self.data['echo_tests']:
            return {'message': 'No echo test data available'}
        
        tests = self.data['echo_tests']
        successful_tests = [t for t in tests if t['status'] == 'completed']
        failed_tests = [t for t in tests if t['status'] != 'completed']
        
        analysis = {
            'total_tests': len(tests),
            'successful_tests': len(successful_tests),
            'failed_tests': len(failed_tests),
            'success_rate': len(successful_tests) / len(tests) * 100 if tests else 0,
            'recent_tests': tests[-5:] if len(tests) > 5 else tests
        }
        
        if successful_tests and any(t.get('response_time') for t in successful_tests):
            response_times = [t['response_time'] for t in successful_tests if t.get('response_time')]
            if response_times:
                analysis['avg_response_time'] = sum(response_times) / len(response_times)
                analysis['min_response_time'] = min(response_times)
                analysis['max_response_time'] = max(response_times)
        
        return analysis
    
    def get_time_sync_analysis(self) -> Dict[str, Any]:
        """Analyze SNTP time synchronization"""
        if not self.data['sntp_checks']:
            return {'message': 'No SNTP check data available'}
        
        checks = self.data['sntp_checks']
        time_differences = [c['time_difference'] for c in checks]
        
        analysis = {
            'total_checks': len(checks),
            'avg_time_difference': sum(time_differences) / len(time_differences),
            'min_time_difference': min(time_differences),
            'max_time_difference': max(time_differences),
            'recent_checks': checks[-3:] if len(checks) > 3 else checks
        }
        
        # Determine sync quality
        avg_diff = analysis['avg_time_difference']
        if avg_diff < 1.0:
            analysis['sync_quality'] = 'Excellent'
        elif avg_diff < 5.0:
            analysis['sync_quality'] = 'Good'
        elif avg_diff < 10.0:
            analysis['sync_quality'] = 'Fair'
        else:
            analysis['sync_quality'] = 'Poor'
        
        return analysis
    
    def get_error_analysis(self) -> Dict[str, Any]:
        """Analyze socket errors across modules"""
        if not self.data['socket_errors']:
            return {'message': 'No error data available'}
        
        errors = self.data['socket_errors']
        
        # Group errors by module
        module_errors = {}
        for error in errors:
            module = error['module']
            if module not in module_errors:
                module_errors[module] = []
            module_errors[module].append(error)
        
        analysis = {
            'total_errors': len(errors),
            'errors_by_module': {module: len(errors) for module, errors in module_errors.items()},
            'recent_errors': errors[-5:] if len(errors) > 5 else errors
        }
        
        return analysis
    
    def get_integration_summary(self) -> Dict[str, Any]:
        """Get overall integration summary"""
        summary = {
            'timestamp': datetime.now().isoformat(),
            'echo_tests': len(self.data['echo_tests']),
            'sntp_checks': len(self.data['sntp_checks']),
            'machine_info_entries': len(self.data['machine_info']),
            'socket_errors': len(self.data['socket_errors']),
            'chat_sessions': len(self.data['chat_sessions']),
            'integration_events': len(self.data['integration_log'])
        }
        
        return summary
    
    def export_data(self, export_file: str = None) -> str:
        """Export all integration data to a file"""
        if export_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            export_file = f"integration_export_{timestamp}.json"
        
        try:
            with open(export_file, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
            return export_file
        except IOError as e:
            raise Exception(f"Failed to export data: {e}")
    
    def clear_old_data(self, days: int = 30):
        """Clear data older than specified days"""
        cutoff_date = datetime.now().timestamp() - (days * 24 * 60 * 60)
        
        for key in ['echo_tests', 'sntp_checks', 'machine_info', 'socket_errors', 'chat_sessions', 'integration_log']:
            if key in self.data:
                self.data[key] = [
                    item for item in self.data[key]
                    if datetime.fromisoformat(item['timestamp']).timestamp() > cutoff_date
                ]
        
        self.save_data()
        self.log_integration('data_cleanup', f"Cleared data older than {days} days")

# Global integrator instance
integrator = DataIntegrator()

def get_integrator() -> DataIntegrator:
    """Get the global integrator instance"""
    return integrator

if __name__ == "__main__":
    # Test the data integrator
    integrator = DataIntegrator()
    
    # Add some test data
    integrator.add_echo_test_result(8880, "completed", 0.05)
    integrator.add_sntp_check("2024-01-01 12:00:00", "2024-01-01 12:00:01", 1.0)
    integrator.add_socket_error("ConnectionError", "Connection refused", "echo_test", 8880)
    
    # Show analysis
    print("Echo Test Analysis:")
    print(json.dumps(integrator.get_echo_test_analysis(), indent=2))
    
    print("\nTime Sync Analysis:")
    print(json.dumps(integrator.get_time_sync_analysis(), indent=2))
    
    print("\nError Analysis:")
    print(json.dumps(integrator.get_error_analysis(), indent=2))
    
    print("\nIntegration Summary:")
    print(json.dumps(integrator.get_integration_summary(), indent=2))
