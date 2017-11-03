from ncclient import manager
from ncclient.xml_ import *

with manager.connect(host="localhost", port=2022, username="admin", password="admin", look_for_keys=False) as m:

    stats_filter = """
                      <statistics xmlns="http://btisystems.com/ns/atlas">
                      	<current>
                      		<entity>
                      			<entityName>och:1/1/2/1/1.1</entityName>
                      			<binLength>
									<length>unTimed</length>
								</binLength>
                      		</entity>
                      	</current>
                      </statistics>
                  """


    result = m.get(('subtree',stats_filter))
    print(result)


