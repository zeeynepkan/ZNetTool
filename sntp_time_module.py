import socket
import struct
import time

NTP_SERVER = "pool.ntp.org"  # Using pool.ntp.org as specified in the objective
TIME1970 = 2208988800

def sntp_client():
    """Retrieve current time from SNTP server and compare with local time"""
    print("Connecting to SNTP server:", NTP_SERVER)
    
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(5)
    data = b'\x1b' + 47 * b'\0'
 
    try:
        client.sendto(data, (NTP_SERVER, 123))
        data, address = client.recvfrom(1024)
        
        if data:
            print('Response received from:', address)
            
        # Parse the time from the response
        t = struct.unpack('!12I', data)[10]
        t -= TIME1970
        
        # Get server time and local time
        server_time = time.ctime(t)
        local_time = time.ctime()
        
        print('\n**** Time Information ****')
        print('Server Time (from SNTP):', server_time)
        print('Local System Time      :', local_time)
        
        # Calculate time difference
        server_timestamp = t
        local_timestamp = time.time()
        time_diff = abs(server_timestamp - local_timestamp)
        
        print(f'\nTime Difference        : {time_diff:.2f} seconds')
        
    except socket.timeout:
        print("Request timed out after 5 seconds. UDP/123 may be blocked by firewall or network policy.")
    except Exception as e:
        print(f"Error retrieving time from server: {e}")
    finally:
        client.close()

if __name__ == '__main__':
    sntp_client()
