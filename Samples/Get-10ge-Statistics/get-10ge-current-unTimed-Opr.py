from ncclient import manager
from ncclient.xml_ import *

with manager.connect(host="localhost", port=2022, username="admin", password="admin", look_for_keys=False) as m:

""" This will return all of the PM intervals for a 10ge: Entity """

    stats_filter = """
                      <statistics xmlns="http://btisystems.com/ns/atlas">
                      	<current>
                      		<entity>
                      			<entityName>10ge:1/1/1/1/1</entityName>
                      		</entity>
                      	</current>
                      </statistics>
                  """


    result = m.get(('subtree',stats_filter))
    print(result)