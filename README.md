# bti-netconf

Some python scripts to pull out statistics from the Juniper BTI 7800 series devices using the NETCONF API. 

# Notes on NETCONF on the BTI 7800 series

* The 7800 series uses TCP 2022 for NETCONF rather than the standard TCP 830
* The namespace for all of the 7800 series yang models is xmlns="http://btisystems.com/ns/atlas"
* Only a small subset of the overall yang models are supported by Juniper for 3rd party use, the full list can be found at: 
  https://www.juniper.net/documentation/en_US/bti-series/bti78004.1/topics/reference/general/r-7800-supported-yang-modules.html
  
* The yang models can be downloaded from Juniper's support website:
  https://www.juniper.net/support/downloads/?p=bti7801#sw
  
