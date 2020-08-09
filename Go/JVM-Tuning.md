## JVM and Application Tuning

--------------------------------
#### Database Connection Pool Hints
- Connection pool size < max thread pool size
- Check cost of connection creation  
  - MySQL connection is - Faster and cheaper to create than PostGreSQL
- Async beans require higher number of connections


**Reap Timeout**
- This is the  timer value for the pool maintenence thread
- Smaller the value greater the accuracy
  - Reap timeout < Unused Timeout 
  - Reap timeout < Aged Timeout

**Unused Timeout**
- Internval value in seconds after which an unused or idle connections is discarded


**Aged Timeout**
- Interval in seconds before a ophysical connection is discarded

**Purge Policy**
- Defines how the connections are purged when a stale connection or fatal connection ever occures
- Possible configuration values are 
    - EntirePool
    - FailingConnectionOnly

**Stuck Time Interval**
- A stuck connection is an active connection that is not responding or returning to the connection pool
- If the pool is stuck , a resource exception is given to all new connection requests until the pool is unstruck.

**Stuck Threshold**
- The number of connections that must be considered stuck for pool to be considered in stuck mode


