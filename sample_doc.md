****************************************************************************************************
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
get_version_string


get_version_string
()
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
has_c


has_c
()
DocString: Is the C extension installed?

.. versionadded:: 1.5
***

####################################################################################################
Connection
Connection to MongoDB.
    
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_acceptable_latency


_BaseObject__get_acceptable_latency
(self)
DocString: Any replica-set member whose ping time is within
secondary_acceptable_latency_ms of the nearest member may accept
reads. Defaults to 15 milliseconds.

See :class:`~pymongo.read_preferences.ReadPreference`.

.. versionadded:: 2.3

.. note:: ``secondary_acceptable_latency_ms`` is ignored when talking
  to a replica set *through* a mongos. The equivalent is the
  localThreshold_ command line option.

.. _localThreshold: http://docs.mongodb.org/manual/reference/mongos/#cmdoption-mongos--localThreshold
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_read_pref


_BaseObject__get_read_pref
(self)
DocString: The read preference mode for this instance.

See :class:`~pymongo.read_preferences.ReadPreference` for
available options.

.. versionadded:: 2.1
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_safe


_BaseObject__get_safe
(self)
DocString: **DEPRECATED:** Use the 'w' :attr:`write_concern` option instead.

Use getlasterror with every write operation?

.. versionadded:: 2.0
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_slave_okay


_BaseObject__get_slave_okay
(self)
DocString: DEPRECATED. Use :attr:`read_preference` instead.

.. versionchanged:: 2.1
   Deprecated slave_okay.
.. versionadded:: 2.0
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_tag_sets


_BaseObject__get_tag_sets
(self)
DocString: Set ``tag_sets`` to a list of dictionaries like [{'dc': 'ny'}] to
read only from members whose ``dc`` tag has the value ``"ny"``.
To specify a priority-order for tag sets, provide a list of
tag sets: ``[{'dc': 'ny'}, {'dc': 'la'}, {}]``. A final, empty tag
set, ``{}``, means "read from any member that matches the mode,
ignoring tags." ReplicaSetConnection tries each set of tags in turn
until it finds a set of tags with at least one matching member.

   .. seealso:: `Data-Center Awareness
       <http://www.mongodb.org/display/DOCS/Data+Center+Awareness>`_

.. versionadded:: 2.3
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_uuid_subtype


_BaseObject__get_uuid_subtype
(self)
DocString: This attribute specifies which BSON Binary subtype is used when
storing UUIDs. Historically UUIDs have been stored as BSON Binary
subtype 3. This attribute is used to switch to the newer BSON Binary
subtype 4. It can also be used to force legacy byte order and subtype
compatibility with the Java and C# drivers. See the :mod:`bson.binary`
module for all options.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_write_concern


_BaseObject__get_write_concern
(self)
DocString: The default write concern for this instance.

Supports dict style access for getting/setting write concern
options. Valid options include:

- `w`: (integer or string) If this is a replica set, write operations
  will block until they have been replicated to the specified number
  or tagged set of servers. `w=<int>` always includes the replica set
  primary (e.g. w=3 means write to the primary and wait until
  replicated to **two** secondaries). **Setting w=0 disables write
  acknowledgement and all other write concern options.**
- `wtimeout`: (integer) Used in conjunction with `w`. Specify a value
  in milliseconds to control how long to wait for write propagation
  to complete. If replication does not complete in the given
  timeframe, a timeout exception is raised.
- `j`: If ``True`` block until write operations have been committed
  to the journal. Cannot be used in combination with `fsync`. Prior
  to MongoDB 2.6 this option was ignored if the server was running
  without journaling. Starting with MongoDB 2.6 write operations will
  fail with an exception if this option is used when the server is
  running without journaling.
- `fsync`: If ``True`` and the server is running without journaling,
  blocks until the server has synced all data files to disk. If the
  server is running with journaling, this acts the same as the `j`
  option, blocking until write operations have been committed to the
  journal. Cannot be used in combination with `j`.

>>> m = pymongo.MongoClient()
>>> m.write_concern
{}
>>> m.write_concern = {'w': 2, 'wtimeout': 1000}
>>> m.write_concern
{'wtimeout': 1000, 'w': 2}
>>> m.write_concern['j'] = True
>>> m.write_concern
{'wtimeout': 1000, 'j': True, 'w': 2}
>>> m.write_concern = {'j': True}
>>> m.write_concern
{'j': True}
>>> # Disable write acknowledgement and write concern
...
>>> m.write_concern['w'] = 0


.. note:: Accessing :attr:`write_concern` returns its value
   (a subclass of :class:`dict`), not a copy.

.. warning:: If you are using :class:`~pymongo.connection.Connection`
   or :class:`~pymongo.replica_set_connection.ReplicaSetConnection`
   make sure you explicitly set ``w`` to 1 (or a greater value) or
   :attr:`safe` to ``True``. Unlike calling
   :meth:`set_lasterror_options`, setting an option in
   :attr:`write_concern` does not implicitly set :attr:`safe`
   to ``True``.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_acceptable_latency


_BaseObject__set_acceptable_latency
(self, value)
DocString: Property setter for secondary_acceptable_latency_ms
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_options


_BaseObject__set_options
(self, options)
DocString: Validates and sets all options passed to this object.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_read_pref


_BaseObject__set_read_pref
(self, value)
DocString: Property setter for read_preference
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_safe


_BaseObject__set_safe
(self, value)
DocString: Property setter for safe
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_safe_option


_BaseObject__set_safe_option
(self, option, value)
DocString: Validates and sets getlasterror options for this
object (Connection, Database, Collection, etc.)
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_slave_okay


_BaseObject__set_slave_okay
(self, value)
DocString: Property setter for slave_okay
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_tag_sets


_BaseObject__set_tag_sets
(self, value)
DocString: Property setter for tag_sets
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_uuid_subtype


_BaseObject__set_uuid_subtype
(self, value)
DocString: Sets the BSON Binary subtype to be used when storing UUIDs.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_write_concern


_BaseObject__set_write_concern
(self, value)
DocString: Property setter for write_concern.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__check_auth


_MongoClient__check_auth
(self, sock_info)
DocString: Authenticate using cached database credentials.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__check_bson_size


_MongoClient__check_bson_size
(self, message)
DocString: Make sure the message doesn't include BSON documents larger
than the connected server will accept.

:Parameters:
  - `message`: message to check
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__check_response_to_last_error


_MongoClient__check_response_to_last_error
(self, response, is_command)
DocString: Check a response to a lastError message for errors.

`response` is a byte string representing a response to the message.
If it represents an error response we raise OperationFailure.

Return the response as a document.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__create_pool


_MongoClient__create_pool
(self, pair)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__ensure_member


_MongoClient__ensure_member
(self)
DocString: Connect and return a Member instance, or raise AutoReconnect.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__find_node


_MongoClient__find_node
(self)
DocString: Find a server suitable for our connection type.

Returns a Member and a set of nodes. Doesn't modify state.

If only one host was supplied to __init__ see if we can connect
to it. Don't check if the host is a master/primary so we can make
a direct connection to read from a secondary or send commands to
an arbiter.

If more than one host was supplied treat them as a seed list for
connecting to a replica set or to support high availability for
mongos. If connecting to a replica set try to find the primary,
and set `nodes` to list of all members.

If a mongos seed list was provided find the "nearest" mongos and
return it, setting `nodes` to all mongoses in the seed list that
are up.

Otherwise we iterate through the list trying to find a host we can
send write operations to.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__member_property


_MongoClient__member_property
(self, attr_name, default=None)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__pick_nearest


_MongoClient__pick_nearest
(self, candidates)
DocString: Return the 'nearest' Member instance based on response time.

Doesn't modify state.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__receive_data_on_socket


_MongoClient__receive_data_on_socket
(self, length, sock_info)
DocString: Lowest level receive operation.

Takes length to receive and repeatedly calls recv until able to
return a buffer of that length, raising ConnectionFailure on error.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__receive_message_on_socket


_MongoClient__receive_message_on_socket
(self, operation, rqst_id, sock_info)
DocString: Receive a message in response to `rqst_id` on `sock`.

Returns the response data with the header removed.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__send_and_receive


_MongoClient__send_and_receive
(self, message, sock_info)
DocString: Send a message on the given socket and return the response data.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__simple_command


_MongoClient__simple_command
(self, sock_info, dbname, spec)
DocString: Send a command to the server. May raise AutoReconnect.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__socket


_MongoClient__socket
(self, member)
DocString: Get a SocketInfo.

Calls disconnect() on error.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__try_node


_MongoClient__try_node
(self, node)
DocString: Try to connect to this node and see if it works for our connection
type. Returns a Member and set of hosts (including this one). Doesn't
modify state.

:Parameters:
 - `node`: The (host, port) pair to try.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__enter__


__enter__
(self)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__eq__


__eq__
(self, other)
DocString: Return self==value.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__exit__


__exit__
(self, exc_type, exc_val, exc_tb)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__getattr__


__getattr__
(self, name)
DocString: Get a database by name.

Raises :class:`~pymongo.errors.InvalidName` if an invalid
database name is used.

:Parameters:
  - `name`: the name of the database to get
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__getitem__


__getitem__
(self, name)
DocString: Get a database by name.

Raises :class:`~pymongo.errors.InvalidName` if an invalid
database name is used.

:Parameters:
  - `name`: the name of the database to get
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__init__


__init__
(self, host=None, port=None, max_pool_size=None, network_timeout=None, document_class=<class 'dict'>, tz_aware=False, _connect=True, **kwargs)
DocString: Create a new connection to a single MongoDB instance at *host:port*.

.. warning::
   **DEPRECATED:** :class:`Connection` is deprecated. Please
   use :class:`~pymongo.mongo_client.MongoClient` instead.

The resultant connection object has connection-pooling built
in. It also performs auto-reconnection when necessary. If an
operation fails because of a connection error,
:class:`~pymongo.errors.ConnectionFailure` is raised. If
auto-reconnection will be performed,
:class:`~pymongo.errors.AutoReconnect` will be
raised. Application code should handle this exception
(recognizing that the operation failed) and then continue to
execute.

Raises :class:`TypeError` if port is not an instance of
``int``. Raises :class:`~pymongo.errors.ConnectionFailure` if
the connection cannot be made.

The `host` parameter can be a full `mongodb URI
<http://dochub.mongodb.org/core/connections>`_, in addition to
a simple hostname. It can also be a list of hostnames or
URIs. Any port specified in the host string(s) will override
the `port` parameter. If multiple mongodb URIs containing
database or auth information are passed, the last database,
username, and password present will be used.  For username and
passwords reserved characters like ':', '/', '+' and '@' must be
escaped following RFC 2396.

:Parameters:
  - `host` (optional): hostname or IP address of the
    instance to connect to, or a mongodb URI, or a list of
    hostnames / mongodb URIs. If `host` is an IPv6 literal
    it must be enclosed in '[' and ']' characters following
    the RFC2732 URL syntax (e.g. '[::1]' for localhost)
  - `port` (optional): port number on which to connect
  - `max_pool_size` (optional): The maximum number of connections
    that the pool will open simultaneously. If this is set, operations
    will block if there are `max_pool_size` outstanding connections
    from the pool. By default the pool size is unlimited.
  - `network_timeout` (optional): timeout (in seconds) to use
    for socket operations - default is no timeout
  - `document_class` (optional): default class to use for
    documents returned from queries on this connection
  - `tz_aware` (optional): if ``True``,
    :class:`~datetime.datetime` instances returned as values
    in a document by this :class:`Connection` will be timezone
    aware (otherwise they will be naive)

  | **Other optional parameters can be passed as keyword arguments:**

  - `socketTimeoutMS`: (integer or None) How long (in milliseconds) a
    send or receive on a socket can take before timing out. Defaults to
    ``None`` (no timeout).
  - `connectTimeoutMS`: (integer or None) How long (in milliseconds) a
    connection can take to be opened before timing out. Defaults to
    ``20000``.
  - `waitQueueTimeoutMS`: (integer or None) How long (in milliseconds)
    a thread will wait for a socket from the pool if the pool has no
    free sockets. Defaults to ``None`` (no timeout).
  - `waitQueueMultiple`: (integer or None) Multiplied by max_pool_size
    to give the number of threads allowed to wait for a socket at one
    time. Defaults to ``None`` (no waiters).
  - `socketKeepAlive`: (boolean) Whether to send periodic keep-alive
    packets on connected sockets. Defaults to ``False`` (do not send
    keep-alive packets).
  - `auto_start_request`: If ``True`` (the default), each thread that
    accesses this Connection has a socket allocated to it for the
    thread's lifetime, or until :meth:`end_request` is called.
  - `use_greenlets`: if ``True``, :meth:`start_request()` will ensure
    that the current greenlet uses the same socket for all operations
    until :meth:`end_request()`. Defaults to ``False``.

  | **Write Concern options:**

  - `safe`: :class:`Connection` **disables** acknowledgement of write
    operations. Use ``safe=True`` to enable write acknowledgement.
  - `w`: (integer or string) If this is a replica set, write operations
    will block until they have been replicated to the specified number
    or tagged set of servers. `w=<int>` always includes the replica set
    primary (e.g. w=3 means write to the primary and wait until
    replicated to **two** secondaries). Implies safe=True.
  - `wtimeout`: (integer) Used in conjunction with `w`. Specify a value
    in milliseconds to control how long to wait for write propagation
    to complete. If replication does not complete in the given
    timeframe, a timeout exception is raised. Implies safe=True.
  - `j`: If ``True`` block until write operations have been committed
    to the journal. Cannot be used in combination with `fsync`. Prior
    to MongoDB 2.6 this option was ignored if the server was running
    without journaling. Starting with MongoDB 2.6 write operations will
    fail with an exception if this option is used when the server is
    running without journaling. Implies safe=True.
  - `fsync`: If ``True`` and the server is running without journaling,
    blocks until the server has synced all data files to disk. If the
    server is running with journaling, this acts the same as the `j`
    option, blocking until write operations have been committed to the
    journal. Cannot be used in combination with `j`. Implies safe=True.

  | **Replica-set keyword arguments for connecting with a replica-set
    - either directly or via a mongos:**
  | (ignored by standalone mongod instances)

  - `slave_okay` or `slaveOk` (deprecated): Use `read_preference`
    instead.
  - `replicaSet`: (string) The name of the replica-set to connect to.
    The driver will verify that the replica-set it connects to matches
    this name. Implies that the hosts specified are a seed list and the
    driver should attempt to find all members of the set. *Ignored by
    mongos*. Defaults to ``None``.
  - `read_preference`: The read preference for this client. If
    connecting to a secondary then a read preference mode *other* than
    PRIMARY is required - otherwise all queries will throw a
    :class:`~pymongo.errors.AutoReconnect` "not master" error.
    See :class:`~pymongo.read_preferences.ReadPreference` for all
    available read preference options. Defaults to ``PRIMARY``.
  - `tag_sets`: Ignored unless connecting to a replica-set via mongos.
    Specify a priority-order for tag sets, provide a list of
    tag sets: ``[{'dc': 'ny'}, {'dc': 'la'}, {}]``. A final, empty tag
    set, ``{}``, means "read from any member that matches the mode,
    ignoring tags. Defaults to ``[{}]``, meaning "ignore members'
    tags."

  | **SSL configuration:**

  - `ssl`: If ``True``, create the connection to the server using SSL.
    Defaults to ``False``.
  - `ssl_keyfile`: The private keyfile used to identify the local
    connection against mongod.  If included with the ``certfile` then
    only the ``ssl_certfile`` is needed.  Implies ``ssl=True``.
    Defaults to ``None``.
  - `ssl_certfile`: The certificate file used to identify the local
    connection against mongod. Implies ``ssl=True``. Defaults to
    ``None``.
  - `ssl_cert_reqs`: The parameter cert_reqs specifies whether a
    certificate is required from the other side of the connection,
    and whether it will be validated if provided. It must be one of the
    three values ``ssl.CERT_NONE`` (certificates ignored),
    ``ssl.CERT_OPTIONAL`` (not required, but validated if provided), or
    ``ssl.CERT_REQUIRED`` (required and validated). If the value of
    this parameter is not ``ssl.CERT_NONE``, then the ``ssl_ca_certs``
    parameter must point to a file of CA certificates.
    Implies ``ssl=True``. Defaults to ``ssl.CERT_NONE``.
  - `ssl_ca_certs`: The ca_certs file contains a set of concatenated
    "certification authority" certificates, which are used to validate
    certificates passed from the other end of the connection.
    Implies ``ssl=True``. Defaults to ``None``.

.. seealso:: :meth:`end_request`
.. versionchanged:: 2.5
   Added additional ssl options
.. versionchanged:: 2.3
   Added support for failover between mongos seed list members.
.. versionchanged:: 2.2
   Added `auto_start_request` option back. Added `use_greenlets`
   option.
.. versionchanged:: 2.1
   Support `w` = integer or string.
   Added `ssl` option.
   DEPRECATED slave_okay/slaveOk.
.. versionchanged:: 2.0
   `slave_okay` is a pure keyword argument. Added support for safe,
   and getlasterror options as keyword arguments.
.. versionchanged:: 1.11
   Added `max_pool_size`. Completely removed previously deprecated
   `pool_size`, `auto_start_request` and `timeout` parameters.
.. versionchanged:: 1.8
   The `host` parameter can now be a full `mongodb URI
   <http://dochub.mongodb.org/core/connections>`_, in addition
   to a simple hostname. It can also be a list of hostnames or
   URIs.
.. versionadded:: 1.8
   The `tz_aware` parameter.
.. versionadded:: 1.7
   The `document_class` parameter.
.. versionadded:: 1.1
   The `network_timeout` parameter.

.. mongodoc:: connections
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__iter__


__iter__
(self)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__ne__


__ne__
(self, other)
DocString: Return self!=value.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__next__


__next__
(self)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__repr__


__repr__
(self)
DocString: Return repr(self).
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_cache_credentials


_cache_credentials
(self, source, credentials, connect=True)
DocString: Add credentials to the database authentication cache
for automatic login when a socket is created. If `connect` is True,
verify the credentials on the server first.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_cache_index


_cache_index
(self, database, collection, index, cache_for)
DocString: Add an index to the index cache for ensure_index operations.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_cached


_cached
(self, dbname, coll, index)
DocString: Test if `index` is cached.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_ensure_connected


_ensure_connected
(self, sync=False)
DocString: Ensure this client instance is connected to a mongod/s.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_exhaust_next


_exhaust_next
(self, sock_info)
DocString: Used with exhaust cursors to get the next batch off the socket.

Can raise AutoReconnect.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_get_wc_override


_get_wc_override
(self)
DocString: Get write concern override.

Used in internal methods that **must** do acknowledged write ops.
We don't want to override user write concern options if write concern
is already enabled.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_get_write_mode


_get_write_mode
(self, safe=None, **options)
DocString: Get the current write mode.

Determines if the current write is safe or not based on the
passed in or inherited safe value, write_concern values, or
passed options.

:Parameters:
    - `safe`: check that the operation succeeded?
    - `**options`: overriding write concern options.

.. versionadded:: 2.3
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_purge_credentials


_purge_credentials
(self, source)
DocString: Purge credentials from the database authentication cache.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_purge_index


_purge_index
(self, database_name, collection_name=None, index_name=None)
DocString: Purge an index from the index cache.

If `index_name` is None purge an entire collection.

If `collection_name` is None purge an entire database.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_send_message


_send_message
(self, message, with_last_error=False, command=False)
DocString: Say something to Mongo.

Raises ConnectionFailure if the message cannot be sent. Raises
OperationFailure if `with_last_error` is ``True`` and the
response to the getLastError call returns an error. Return the
response from lastError, or ``None`` if `with_last_error`
is ``False``.

:Parameters:
  - `message`: message to send
  - `with_last_error`: check getLastError status after sending the
    message
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_send_message_with_response


_send_message_with_response
(self, message, _must_use_master=False, **kwargs)
DocString: Send a message to Mongo and return the response.

Sends the given message and returns the response.

:Parameters:
  - `message`: (request_id, data) pair making up the message to send
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
alive


alive
(self)
DocString: Return ``False`` if there has been an error communicating with the
server, else ``True``.

This method attempts to check the status of the server with minimal I/O.
The current thread / greenlet retrieves a socket from the pool (its
request socket if it's in a request, or a random idle socket if it's not
in a request) and checks whether calling `select`_ on it raises an
error. If there are currently no idle sockets, :meth:`alive` will
attempt to actually connect to the server.

A more certain way to determine server availability is::

    client.admin.command('ping')

.. _select: http://docs.python.org/2/library/select.html#select.select
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
close


close
(self)
DocString: Alias for :meth:`disconnect`

Disconnecting will close all underlying sockets in the connection
pool. If this instance is used again it will be automatically
re-opened. Care should be taken to make sure that :meth:`disconnect`
is not called in the middle of a sequence of operations in which
ordering is important. This could lead to unexpected results.

.. seealso:: :meth:`end_request`
.. versionadded:: 2.1
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
close_cursor


close_cursor
(self, cursor_id)
DocString: Close a single database cursor.

Raises :class:`TypeError` if `cursor_id` is not an instance of
``(int, long)``. What closing the cursor actually means
depends on this client's cursor manager.

:Parameters:
  - `cursor_id`: id of cursor to close
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
copy_database


copy_database
(self, from_name, to_name, from_host=None, username=None, password=None, mechanism='DEFAULT')
DocString: **DEPRECATED**: Copy a database, potentially from another host.

:meth:`copy_database` will be removed in PyMongo 3.0. See the
:doc:`copy_database examples </examples/copydb>` for alternatives.

Raises :class:`TypeError` if `from_name` or `to_name` is not
an instance of :class:`basestring` (:class:`str` in python 3).
Raises :class:`~pymongo.errors.InvalidName` if `to_name` is
not a valid database name.

If `from_host` is ``None`` the current host is used as the
source. Otherwise the database is copied from `from_host`.

If the source database requires authentication, `username` and
`password` must be specified. By default, use SCRAM-SHA-1 with
MongoDB 3.0 and later, MONGODB-CR (MongoDB Challenge Response
protocol) for older servers.

.. note:: mongos does not support copying a database from a server
   with authentication, see
   `SERVER-6427 <https://jira.mongodb.org/browse/SERVER-6427>`_.

:Parameters:
  - `from_name`: the name of the source database
  - `to_name`: the name of the target database
  - `from_host` (optional): host name to copy from
  - `username` (optional): username for source database
  - `password` (optional): password for source database
  - `mechanism` (optional): auth method, 'MONGODB-CR' or 'SCRAM-SHA-1'

.. versionchanged:: 2.8
   Deprecated copy_database, and added SCRAM-SHA-1 support.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
database_names


database_names
(self)
DocString: Get a list of the names of all databases on the connected server.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
disconnect


disconnect
(self)
DocString: Disconnect from MongoDB.

Disconnecting will close all underlying sockets in the connection
pool. If this instance is used again it will be automatically
re-opened. Care should be taken to make sure that :meth:`disconnect`
is not called in the middle of a sequence of operations in which
ordering is important. This could lead to unexpected results.

.. seealso:: :meth:`end_request`
.. versionadded:: 1.3
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
drop_database


drop_database
(self, name_or_database)
DocString: Drop a database.

Raises :class:`TypeError` if `name_or_database` is not an instance of
:class:`basestring` (:class:`str` in python 3) or Database.

:Parameters:
  - `name_or_database`: the name of a database to drop, or a
    :class:`~pymongo.database.Database` instance representing the
    database to drop
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
end_request


end_request
(self)
DocString: **DEPRECATED**: Undo :meth:`start_request`. If :meth:`end_request`
is called as many times as :meth:`start_request`, the request is over
and this thread's connection returns to the pool. Extra calls to
:meth:`end_request` have no effect.

Ending a request allows the :class:`~socket.socket` that has
been reserved for this thread by :meth:`start_request` to be returned to
the pool. Other threads will then be able to re-use that
:class:`~socket.socket`. If your application uses many threads, or has
long-running threads that infrequently perform MongoDB operations, then
judicious use of this method can lead to performance gains. Care should
be taken, however, to make sure that :meth:`end_request` is not called
in the middle of a sequence of operations in which ordering is
important. This could lead to unexpected results.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
fsync


fsync
(self, **kwargs)
DocString: Flush all pending writes to datafiles.

:Parameters:

    Optional parameters can be passed as keyword arguments:

    - `lock`: If True lock the server to disallow writes.
    - `async`: If True don't block while synchronizing.

    .. warning:: `async` and `lock` can not be used together.

    .. warning:: MongoDB does not support the `async` option
                 on Windows and will raise an exception on that
                 platform.

.. versionadded:: 2.0
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
get_default_database


get_default_database
(self)
DocString: Get the database named in the MongoDB connection URI.

>>> uri = 'mongodb://host/my_database'
>>> client = MongoClient(uri)
>>> db = client.get_default_database()
>>> assert db.name == 'my_database'

Useful in scripts where you want to choose which database to use
based only on the URI in a configuration file.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
get_document_class


get_document_class
(self)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
get_lasterror_options


get_lasterror_options
(self)
DocString: DEPRECATED: Use :attr:`write_concern` instead.

Returns a dict of the getlasterror options set on this instance.

.. versionchanged:: 2.4
   Deprecated get_lasterror_options.
.. versionadded:: 2.0
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
in_request


in_request
(self)
DocString: **DEPRECATED**: True if this thread is in a request, meaning it has
a socket reserved for its exclusive use.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
kill_cursors


kill_cursors
(self, cursor_ids)
DocString: Send a kill cursors message with the given ids.

Raises :class:`TypeError` if `cursor_ids` is not an instance of
``list``.

:Parameters:
  - `cursor_ids`: list of cursor ids to kill
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
server_info


server_info
(self)
DocString: Get information about the MongoDB server we're connected to.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
set_cursor_manager


set_cursor_manager
(self, manager_class)
DocString: Set this client's cursor manager.

Raises :class:`TypeError` if `manager_class` is not a subclass of
:class:`~pymongo.cursor_manager.CursorManager`. A cursor manager
handles closing cursors. Different managers can implement different
policies in terms of when to actually kill a cursor that has
been closed.

:Parameters:
  - `manager_class`: cursor manager to use

.. versionchanged:: 2.1+
   Deprecated support for external cursor managers.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
set_document_class


set_document_class
(self, klass)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
set_lasterror_options


set_lasterror_options
(self, **kwargs)
DocString: DEPRECATED: Use :attr:`write_concern` instead.

Set getlasterror options for this instance.

Valid options include j=<bool>, w=<int/string>, wtimeout=<int>,
and fsync=<bool>. Implies safe=True.

:Parameters:
    - `**kwargs`: Options should be passed as keyword
                  arguments (e.g. w=2, fsync=True)

.. versionchanged:: 2.4
   Deprecated set_lasterror_options.
.. versionadded:: 2.0
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
start_request


start_request
(self)
DocString: **DEPRECATED**: start_request will be removed in PyMongo 3.0.

When doing w=0 writes to MongoDB 2.4 or earlier, :meth:`start_request`
was sometimes useful to ensure the current thread always used the same
socket until it called :meth:`end_request`. This made consistent reads
more likely after an unacknowledged write. Requests are no longer
useful in modern MongoDB applications, see
`PYTHON-785 <https://jira.mongodb.org/browse/PYTHON-785>`_.

.. versionchanged:: 2.8
   Deprecated.

.. versionchanged:: 2.4
   Now counts the number of calls to start_request and doesn't end
   request until an equal number of calls to end_request.

.. versionadded:: 2.2
   The :class:`~pymongo.pool.Request` return value.
   :meth:`start_request` previously returned None
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
unlock


unlock
(self)
DocString: Unlock a previously locked server.

.. versionadded:: 2.0
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
unset_lasterror_options


unset_lasterror_options
(self, *options)
DocString: DEPRECATED: Use :attr:`write_concern` instead.

Unset getlasterror options for this instance.

If no options are passed unsets all getlasterror options.
This does not set `safe` to False.

:Parameters:
    - `*options`: The list of options to unset.

.. versionchanged:: 2.4
   Deprecated unset_lasterror_options.
.. versionadded:: 2.0
####################################################################################################
MongoClient
Connection to MongoDB.
    
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_acceptable_latency


_BaseObject__get_acceptable_latency
(self)
DocString: Any replica-set member whose ping time is within
secondary_acceptable_latency_ms of the nearest member may accept
reads. Defaults to 15 milliseconds.

See :class:`~pymongo.read_preferences.ReadPreference`.

.. versionadded:: 2.3

.. note:: ``secondary_acceptable_latency_ms`` is ignored when talking
  to a replica set *through* a mongos. The equivalent is the
  localThreshold_ command line option.

.. _localThreshold: http://docs.mongodb.org/manual/reference/mongos/#cmdoption-mongos--localThreshold
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_read_pref


_BaseObject__get_read_pref
(self)
DocString: The read preference mode for this instance.

See :class:`~pymongo.read_preferences.ReadPreference` for
available options.

.. versionadded:: 2.1
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_safe


_BaseObject__get_safe
(self)
DocString: **DEPRECATED:** Use the 'w' :attr:`write_concern` option instead.

Use getlasterror with every write operation?

.. versionadded:: 2.0
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_slave_okay


_BaseObject__get_slave_okay
(self)
DocString: DEPRECATED. Use :attr:`read_preference` instead.

.. versionchanged:: 2.1
   Deprecated slave_okay.
.. versionadded:: 2.0
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_tag_sets


_BaseObject__get_tag_sets
(self)
DocString: Set ``tag_sets`` to a list of dictionaries like [{'dc': 'ny'}] to
read only from members whose ``dc`` tag has the value ``"ny"``.
To specify a priority-order for tag sets, provide a list of
tag sets: ``[{'dc': 'ny'}, {'dc': 'la'}, {}]``. A final, empty tag
set, ``{}``, means "read from any member that matches the mode,
ignoring tags." ReplicaSetConnection tries each set of tags in turn
until it finds a set of tags with at least one matching member.

   .. seealso:: `Data-Center Awareness
       <http://www.mongodb.org/display/DOCS/Data+Center+Awareness>`_

.. versionadded:: 2.3
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_uuid_subtype


_BaseObject__get_uuid_subtype
(self)
DocString: This attribute specifies which BSON Binary subtype is used when
storing UUIDs. Historically UUIDs have been stored as BSON Binary
subtype 3. This attribute is used to switch to the newer BSON Binary
subtype 4. It can also be used to force legacy byte order and subtype
compatibility with the Java and C# drivers. See the :mod:`bson.binary`
module for all options.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_write_concern


_BaseObject__get_write_concern
(self)
DocString: The default write concern for this instance.

Supports dict style access for getting/setting write concern
options. Valid options include:

- `w`: (integer or string) If this is a replica set, write operations
  will block until they have been replicated to the specified number
  or tagged set of servers. `w=<int>` always includes the replica set
  primary (e.g. w=3 means write to the primary and wait until
  replicated to **two** secondaries). **Setting w=0 disables write
  acknowledgement and all other write concern options.**
- `wtimeout`: (integer) Used in conjunction with `w`. Specify a value
  in milliseconds to control how long to wait for write propagation
  to complete. If replication does not complete in the given
  timeframe, a timeout exception is raised.
- `j`: If ``True`` block until write operations have been committed
  to the journal. Cannot be used in combination with `fsync`. Prior
  to MongoDB 2.6 this option was ignored if the server was running
  without journaling. Starting with MongoDB 2.6 write operations will
  fail with an exception if this option is used when the server is
  running without journaling.
- `fsync`: If ``True`` and the server is running without journaling,
  blocks until the server has synced all data files to disk. If the
  server is running with journaling, this acts the same as the `j`
  option, blocking until write operations have been committed to the
  journal. Cannot be used in combination with `j`.

>>> m = pymongo.MongoClient()
>>> m.write_concern
{}
>>> m.write_concern = {'w': 2, 'wtimeout': 1000}
>>> m.write_concern
{'wtimeout': 1000, 'w': 2}
>>> m.write_concern['j'] = True
>>> m.write_concern
{'wtimeout': 1000, 'j': True, 'w': 2}
>>> m.write_concern = {'j': True}
>>> m.write_concern
{'j': True}
>>> # Disable write acknowledgement and write concern
...
>>> m.write_concern['w'] = 0


.. note:: Accessing :attr:`write_concern` returns its value
   (a subclass of :class:`dict`), not a copy.

.. warning:: If you are using :class:`~pymongo.connection.Connection`
   or :class:`~pymongo.replica_set_connection.ReplicaSetConnection`
   make sure you explicitly set ``w`` to 1 (or a greater value) or
   :attr:`safe` to ``True``. Unlike calling
   :meth:`set_lasterror_options`, setting an option in
   :attr:`write_concern` does not implicitly set :attr:`safe`
   to ``True``.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_acceptable_latency


_BaseObject__set_acceptable_latency
(self, value)
DocString: Property setter for secondary_acceptable_latency_ms
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_options


_BaseObject__set_options
(self, options)
DocString: Validates and sets all options passed to this object.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_read_pref


_BaseObject__set_read_pref
(self, value)
DocString: Property setter for read_preference
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_safe


_BaseObject__set_safe
(self, value)
DocString: Property setter for safe
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_safe_option


_BaseObject__set_safe_option
(self, option, value)
DocString: Validates and sets getlasterror options for this
object (Connection, Database, Collection, etc.)
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_slave_okay


_BaseObject__set_slave_okay
(self, value)
DocString: Property setter for slave_okay
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_tag_sets


_BaseObject__set_tag_sets
(self, value)
DocString: Property setter for tag_sets
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_uuid_subtype


_BaseObject__set_uuid_subtype
(self, value)
DocString: Sets the BSON Binary subtype to be used when storing UUIDs.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_write_concern


_BaseObject__set_write_concern
(self, value)
DocString: Property setter for write_concern.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__check_auth


_MongoClient__check_auth
(self, sock_info)
DocString: Authenticate using cached database credentials.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__check_bson_size


_MongoClient__check_bson_size
(self, message)
DocString: Make sure the message doesn't include BSON documents larger
than the connected server will accept.

:Parameters:
  - `message`: message to check
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__check_response_to_last_error


_MongoClient__check_response_to_last_error
(self, response, is_command)
DocString: Check a response to a lastError message for errors.

`response` is a byte string representing a response to the message.
If it represents an error response we raise OperationFailure.

Return the response as a document.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__create_pool


_MongoClient__create_pool
(self, pair)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__ensure_member


_MongoClient__ensure_member
(self)
DocString: Connect and return a Member instance, or raise AutoReconnect.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__find_node


_MongoClient__find_node
(self)
DocString: Find a server suitable for our connection type.

Returns a Member and a set of nodes. Doesn't modify state.

If only one host was supplied to __init__ see if we can connect
to it. Don't check if the host is a master/primary so we can make
a direct connection to read from a secondary or send commands to
an arbiter.

If more than one host was supplied treat them as a seed list for
connecting to a replica set or to support high availability for
mongos. If connecting to a replica set try to find the primary,
and set `nodes` to list of all members.

If a mongos seed list was provided find the "nearest" mongos and
return it, setting `nodes` to all mongoses in the seed list that
are up.

Otherwise we iterate through the list trying to find a host we can
send write operations to.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__member_property


_MongoClient__member_property
(self, attr_name, default=None)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__pick_nearest


_MongoClient__pick_nearest
(self, candidates)
DocString: Return the 'nearest' Member instance based on response time.

Doesn't modify state.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__receive_data_on_socket


_MongoClient__receive_data_on_socket
(self, length, sock_info)
DocString: Lowest level receive operation.

Takes length to receive and repeatedly calls recv until able to
return a buffer of that length, raising ConnectionFailure on error.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__receive_message_on_socket


_MongoClient__receive_message_on_socket
(self, operation, rqst_id, sock_info)
DocString: Receive a message in response to `rqst_id` on `sock`.

Returns the response data with the header removed.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__send_and_receive


_MongoClient__send_and_receive
(self, message, sock_info)
DocString: Send a message on the given socket and return the response data.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__simple_command


_MongoClient__simple_command
(self, sock_info, dbname, spec)
DocString: Send a command to the server. May raise AutoReconnect.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__socket


_MongoClient__socket
(self, member)
DocString: Get a SocketInfo.

Calls disconnect() on error.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoClient__try_node


_MongoClient__try_node
(self, node)
DocString: Try to connect to this node and see if it works for our connection
type. Returns a Member and set of hosts (including this one). Doesn't
modify state.

:Parameters:
 - `node`: The (host, port) pair to try.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__enter__


__enter__
(self)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__eq__


__eq__
(self, other)
DocString: Return self==value.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__exit__


__exit__
(self, exc_type, exc_val, exc_tb)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__getattr__


__getattr__
(self, name)
DocString: Get a database by name.

Raises :class:`~pymongo.errors.InvalidName` if an invalid
database name is used.

:Parameters:
  - `name`: the name of the database to get
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__getitem__


__getitem__
(self, name)
DocString: Get a database by name.

Raises :class:`~pymongo.errors.InvalidName` if an invalid
database name is used.

:Parameters:
  - `name`: the name of the database to get
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__init__


__init__
(self, host=None, port=None, max_pool_size=100, document_class=<class 'dict'>, tz_aware=False, _connect=True, **kwargs)
DocString: Create a new connection to a single MongoDB instance at *host:port*.

The resultant client object has connection-pooling built
in. It also performs auto-reconnection when necessary. If an
operation fails because of a connection error,
:class:`~pymongo.errors.ConnectionFailure` is raised. If
auto-reconnection will be performed,
:class:`~pymongo.errors.AutoReconnect` will be
raised. Application code should handle this exception
(recognizing that the operation failed) and then continue to
execute.

Raises :class:`TypeError` if port is not an instance of
``int``. Raises :class:`~pymongo.errors.ConnectionFailure` if
the connection cannot be made.

The `host` parameter can be a full `mongodb URI
<http://dochub.mongodb.org/core/connections>`_, in addition to
a simple hostname. It can also be a list of hostnames or
URIs. Any port specified in the host string(s) will override
the `port` parameter. If multiple mongodb URIs containing
database or auth information are passed, the last database,
username, and password present will be used.  For username and
passwords reserved characters like ':', '/', '+' and '@' must be
escaped following RFC 2396.

:Parameters:
  - `host` (optional): hostname or IP address of the
    instance to connect to, or a mongodb URI, or a list of
    hostnames / mongodb URIs. If `host` is an IPv6 literal
    it must be enclosed in '[' and ']' characters following
    the RFC2732 URL syntax (e.g. '[::1]' for localhost)
  - `port` (optional): port number on which to connect
  - `max_pool_size` (optional): The maximum number of connections
    that the pool will open simultaneously. If this is set, operations
    will block if there are `max_pool_size` outstanding connections
    from the pool. Defaults to 100.
  - `document_class` (optional): default class to use for
    documents returned from queries on this client
  - `tz_aware` (optional): if ``True``,
    :class:`~datetime.datetime` instances returned as values
    in a document by this :class:`MongoClient` will be timezone
    aware (otherwise they will be naive)

  | **Other optional parameters can be passed as keyword arguments:**

  - `socketTimeoutMS`: (integer or None) How long (in milliseconds) a
    send or receive on a socket can take before timing out. Defaults to
    ``None`` (no timeout).
  - `connectTimeoutMS`: (integer or None) How long (in milliseconds) a
    connection can take to be opened before timing out. Defaults to
    ``20000``.
  - `waitQueueTimeoutMS`: (integer or None) How long (in milliseconds)
    a thread will wait for a socket from the pool if the pool has no
    free sockets. Defaults to ``None`` (no timeout).
  - `waitQueueMultiple`: (integer or None) Multiplied by max_pool_size
    to give the number of threads allowed to wait for a socket at one
    time. Defaults to ``None`` (no waiters).
  - `socketKeepAlive`: (boolean) Whether to send periodic keep-alive
    packets on connected sockets. Defaults to ``False`` (do not send
    keep-alive packets).
  - `auto_start_request`: Deprecated.
  - `use_greenlets`: If ``True``, :meth:`start_request()` will ensure
    that the current greenlet uses the same socket for all
    operations until :meth:`end_request()`. Defaults to ``False``.

  | **Write Concern options:**
  | (Only set if passed. No default values.)

  - `w`: (integer or string) If this is a replica set, write operations
    will block until they have been replicated to the specified number
    or tagged set of servers. `w=<int>` always includes the replica set
    primary (e.g. w=3 means write to the primary and wait until
    replicated to **two** secondaries). Passing w=0 **disables write
    acknowledgement** and all other write concern options.
  - `wtimeout`: (integer) Used in conjunction with `w`. Specify a value
    in milliseconds to control how long to wait for write propagation
    to complete. If replication does not complete in the given
    timeframe, a timeout exception is raised.
  - `j`: If ``True`` block until write operations have been committed
    to the journal. Cannot be used in combination with `fsync`. Prior
    to MongoDB 2.6 this option was ignored if the server was running
    without journaling. Starting with MongoDB 2.6 write operations will
    fail with an exception if this option is used when the server is
    running without journaling.
  - `fsync`: If ``True`` and the server is running without journaling,
    blocks until the server has synced all data files to disk. If the
    server is running with journaling, this acts the same as the `j`
    option, blocking until write operations have been committed to the
    journal. Cannot be used in combination with `j`.

  | **Replica set keyword arguments for connecting with a replica set
    - either directly or via a mongos:**
  | (ignored by standalone mongod instances)

  - `replicaSet`: (string or None) The name of the replica set to
    connect to. The driver will verify that the replica set it connects
    to matches this name. Implies that the hosts specified are a seed
    list and the driver should attempt to find all members of the set.
    *Ignored by mongos*. Defaults to ``None``.
  - `read_preference`: The read preference for this client. If
    connecting to a secondary then a read preference mode *other* than
    PRIMARY is required - otherwise all queries will throw
    :class:`~pymongo.errors.AutoReconnect` "not master".
    See :class:`~pymongo.read_preferences.ReadPreference` for all
    available read preference options. Defaults to ``PRIMARY``.
  - `tag_sets`: Ignored unless connecting to a replica set via mongos.
    Specify a priority-order for tag sets, provide a list of
    tag sets: ``[{'dc': 'ny'}, {'dc': 'la'}, {}]``. A final, empty tag
    set, ``{}``, means "read from any member that matches the mode,
    ignoring tags. Defaults to ``[{}]``, meaning "ignore members'
    tags."

  | **SSL configuration:**

  - `ssl`: If ``True``, create the connection to the server using SSL.
    Defaults to ``False``.
  - `ssl_keyfile`: The private keyfile used to identify the local
    connection against mongod.  If included with the ``certfile`` then
    only the ``ssl_certfile`` is needed.  Implies ``ssl=True``.
    Defaults to ``None``.
  - `ssl_certfile`: The certificate file used to identify the local
    connection against mongod. Implies ``ssl=True``. Defaults to
    ``None``.
  - `ssl_cert_reqs`: Specifies whether a certificate is required from
    the other side of the connection, and whether it will be validated
    if provided. It must be one of the three values ``ssl.CERT_NONE``
    (certificates ignored), ``ssl.CERT_OPTIONAL``
    (not required, but validated if provided), or ``ssl.CERT_REQUIRED``
    (required and validated). If the value of this parameter is not
    ``ssl.CERT_NONE``, then the ``ssl_ca_certs`` parameter must point
    to a file of CA certificates. Implies ``ssl=True``. Defaults to
    ``ssl.CERT_NONE``.
  - `ssl_ca_certs`: The ca_certs file contains a set of concatenated
    "certification authority" certificates, which are used to validate
    certificates passed from the other end of the connection.
    Implies ``ssl=True``. Defaults to ``None``.

.. seealso:: :meth:`end_request`

.. mongodoc:: connections

.. versionchanged:: 2.5
   Added additional ssl options
.. versionadded:: 2.4
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__iter__


__iter__
(self)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__ne__


__ne__
(self, other)
DocString: Return self!=value.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__next__


__next__
(self)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__repr__


__repr__
(self)
DocString: Return repr(self).
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_cache_credentials


_cache_credentials
(self, source, credentials, connect=True)
DocString: Add credentials to the database authentication cache
for automatic login when a socket is created. If `connect` is True,
verify the credentials on the server first.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_cache_index


_cache_index
(self, database, collection, index, cache_for)
DocString: Add an index to the index cache for ensure_index operations.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_cached


_cached
(self, dbname, coll, index)
DocString: Test if `index` is cached.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_ensure_connected


_ensure_connected
(self, sync=False)
DocString: Ensure this client instance is connected to a mongod/s.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_exhaust_next


_exhaust_next
(self, sock_info)
DocString: Used with exhaust cursors to get the next batch off the socket.

Can raise AutoReconnect.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_get_wc_override


_get_wc_override
(self)
DocString: Get write concern override.

Used in internal methods that **must** do acknowledged write ops.
We don't want to override user write concern options if write concern
is already enabled.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_get_write_mode


_get_write_mode
(self, safe=None, **options)
DocString: Get the current write mode.

Determines if the current write is safe or not based on the
passed in or inherited safe value, write_concern values, or
passed options.

:Parameters:
    - `safe`: check that the operation succeeded?
    - `**options`: overriding write concern options.

.. versionadded:: 2.3
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_purge_credentials


_purge_credentials
(self, source)
DocString: Purge credentials from the database authentication cache.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_purge_index


_purge_index
(self, database_name, collection_name=None, index_name=None)
DocString: Purge an index from the index cache.

If `index_name` is None purge an entire collection.

If `collection_name` is None purge an entire database.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_send_message


_send_message
(self, message, with_last_error=False, command=False)
DocString: Say something to Mongo.

Raises ConnectionFailure if the message cannot be sent. Raises
OperationFailure if `with_last_error` is ``True`` and the
response to the getLastError call returns an error. Return the
response from lastError, or ``None`` if `with_last_error`
is ``False``.

:Parameters:
  - `message`: message to send
  - `with_last_error`: check getLastError status after sending the
    message
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_send_message_with_response


_send_message_with_response
(self, message, _must_use_master=False, **kwargs)
DocString: Send a message to Mongo and return the response.

Sends the given message and returns the response.

:Parameters:
  - `message`: (request_id, data) pair making up the message to send
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
alive


alive
(self)
DocString: Return ``False`` if there has been an error communicating with the
server, else ``True``.

This method attempts to check the status of the server with minimal I/O.
The current thread / greenlet retrieves a socket from the pool (its
request socket if it's in a request, or a random idle socket if it's not
in a request) and checks whether calling `select`_ on it raises an
error. If there are currently no idle sockets, :meth:`alive` will
attempt to actually connect to the server.

A more certain way to determine server availability is::

    client.admin.command('ping')

.. _select: http://docs.python.org/2/library/select.html#select.select
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
close


close
(self)
DocString: Alias for :meth:`disconnect`

Disconnecting will close all underlying sockets in the connection
pool. If this instance is used again it will be automatically
re-opened. Care should be taken to make sure that :meth:`disconnect`
is not called in the middle of a sequence of operations in which
ordering is important. This could lead to unexpected results.

.. seealso:: :meth:`end_request`
.. versionadded:: 2.1
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
close_cursor


close_cursor
(self, cursor_id)
DocString: Close a single database cursor.

Raises :class:`TypeError` if `cursor_id` is not an instance of
``(int, long)``. What closing the cursor actually means
depends on this client's cursor manager.

:Parameters:
  - `cursor_id`: id of cursor to close
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
copy_database


copy_database
(self, from_name, to_name, from_host=None, username=None, password=None, mechanism='DEFAULT')
DocString: **DEPRECATED**: Copy a database, potentially from another host.

:meth:`copy_database` will be removed in PyMongo 3.0. See the
:doc:`copy_database examples </examples/copydb>` for alternatives.

Raises :class:`TypeError` if `from_name` or `to_name` is not
an instance of :class:`basestring` (:class:`str` in python 3).
Raises :class:`~pymongo.errors.InvalidName` if `to_name` is
not a valid database name.

If `from_host` is ``None`` the current host is used as the
source. Otherwise the database is copied from `from_host`.

If the source database requires authentication, `username` and
`password` must be specified. By default, use SCRAM-SHA-1 with
MongoDB 3.0 and later, MONGODB-CR (MongoDB Challenge Response
protocol) for older servers.

.. note:: mongos does not support copying a database from a server
   with authentication, see
   `SERVER-6427 <https://jira.mongodb.org/browse/SERVER-6427>`_.

:Parameters:
  - `from_name`: the name of the source database
  - `to_name`: the name of the target database
  - `from_host` (optional): host name to copy from
  - `username` (optional): username for source database
  - `password` (optional): password for source database
  - `mechanism` (optional): auth method, 'MONGODB-CR' or 'SCRAM-SHA-1'

.. versionchanged:: 2.8
   Deprecated copy_database, and added SCRAM-SHA-1 support.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
database_names


database_names
(self)
DocString: Get a list of the names of all databases on the connected server.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
disconnect


disconnect
(self)
DocString: Disconnect from MongoDB.

Disconnecting will close all underlying sockets in the connection
pool. If this instance is used again it will be automatically
re-opened. Care should be taken to make sure that :meth:`disconnect`
is not called in the middle of a sequence of operations in which
ordering is important. This could lead to unexpected results.

.. seealso:: :meth:`end_request`
.. versionadded:: 1.3
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
drop_database


drop_database
(self, name_or_database)
DocString: Drop a database.

Raises :class:`TypeError` if `name_or_database` is not an instance of
:class:`basestring` (:class:`str` in python 3) or Database.

:Parameters:
  - `name_or_database`: the name of a database to drop, or a
    :class:`~pymongo.database.Database` instance representing the
    database to drop
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
end_request


end_request
(self)
DocString: **DEPRECATED**: Undo :meth:`start_request`. If :meth:`end_request`
is called as many times as :meth:`start_request`, the request is over
and this thread's connection returns to the pool. Extra calls to
:meth:`end_request` have no effect.

Ending a request allows the :class:`~socket.socket` that has
been reserved for this thread by :meth:`start_request` to be returned to
the pool. Other threads will then be able to re-use that
:class:`~socket.socket`. If your application uses many threads, or has
long-running threads that infrequently perform MongoDB operations, then
judicious use of this method can lead to performance gains. Care should
be taken, however, to make sure that :meth:`end_request` is not called
in the middle of a sequence of operations in which ordering is
important. This could lead to unexpected results.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
fsync


fsync
(self, **kwargs)
DocString: Flush all pending writes to datafiles.

:Parameters:

    Optional parameters can be passed as keyword arguments:

    - `lock`: If True lock the server to disallow writes.
    - `async`: If True don't block while synchronizing.

    .. warning:: `async` and `lock` can not be used together.

    .. warning:: MongoDB does not support the `async` option
                 on Windows and will raise an exception on that
                 platform.

.. versionadded:: 2.0
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
get_default_database


get_default_database
(self)
DocString: Get the database named in the MongoDB connection URI.

>>> uri = 'mongodb://host/my_database'
>>> client = MongoClient(uri)
>>> db = client.get_default_database()
>>> assert db.name == 'my_database'

Useful in scripts where you want to choose which database to use
based only on the URI in a configuration file.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
get_document_class


get_document_class
(self)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
get_lasterror_options


get_lasterror_options
(self)
DocString: DEPRECATED: Use :attr:`write_concern` instead.

Returns a dict of the getlasterror options set on this instance.

.. versionchanged:: 2.4
   Deprecated get_lasterror_options.
.. versionadded:: 2.0
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
in_request


in_request
(self)
DocString: **DEPRECATED**: True if this thread is in a request, meaning it has
a socket reserved for its exclusive use.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
kill_cursors


kill_cursors
(self, cursor_ids)
DocString: Send a kill cursors message with the given ids.

Raises :class:`TypeError` if `cursor_ids` is not an instance of
``list``.

:Parameters:
  - `cursor_ids`: list of cursor ids to kill
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
server_info


server_info
(self)
DocString: Get information about the MongoDB server we're connected to.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
set_cursor_manager


set_cursor_manager
(self, manager_class)
DocString: Set this client's cursor manager.

Raises :class:`TypeError` if `manager_class` is not a subclass of
:class:`~pymongo.cursor_manager.CursorManager`. A cursor manager
handles closing cursors. Different managers can implement different
policies in terms of when to actually kill a cursor that has
been closed.

:Parameters:
  - `manager_class`: cursor manager to use

.. versionchanged:: 2.1+
   Deprecated support for external cursor managers.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
set_document_class


set_document_class
(self, klass)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
set_lasterror_options


set_lasterror_options
(self, **kwargs)
DocString: DEPRECATED: Use :attr:`write_concern` instead.

Set getlasterror options for this instance.

Valid options include j=<bool>, w=<int/string>, wtimeout=<int>,
and fsync=<bool>. Implies safe=True.

:Parameters:
    - `**kwargs`: Options should be passed as keyword
                  arguments (e.g. w=2, fsync=True)

.. versionchanged:: 2.4
   Deprecated set_lasterror_options.
.. versionadded:: 2.0
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
start_request


start_request
(self)
DocString: **DEPRECATED**: start_request will be removed in PyMongo 3.0.

When doing w=0 writes to MongoDB 2.4 or earlier, :meth:`start_request`
was sometimes useful to ensure the current thread always used the same
socket until it called :meth:`end_request`. This made consistent reads
more likely after an unacknowledged write. Requests are no longer
useful in modern MongoDB applications, see
`PYTHON-785 <https://jira.mongodb.org/browse/PYTHON-785>`_.

.. versionchanged:: 2.8
   Deprecated.

.. versionchanged:: 2.4
   Now counts the number of calls to start_request and doesn't end
   request until an equal number of calls to end_request.

.. versionadded:: 2.2
   The :class:`~pymongo.pool.Request` return value.
   :meth:`start_request` previously returned None
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
unlock


unlock
(self)
DocString: Unlock a previously locked server.

.. versionadded:: 2.0
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
unset_lasterror_options


unset_lasterror_options
(self, *options)
DocString: DEPRECATED: Use :attr:`write_concern` instead.

Unset getlasterror options for this instance.

If no options are passed unsets all getlasterror options.
This does not set `safe` to False.

:Parameters:
    - `*options`: The list of options to unset.

.. versionchanged:: 2.4
   Deprecated unset_lasterror_options.
.. versionadded:: 2.0
####################################################################################################
MongoReplicaSetClient
Connection to a MongoDB replica set.
    
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_acceptable_latency


_BaseObject__get_acceptable_latency
(self)
DocString: Any replica-set member whose ping time is within
secondary_acceptable_latency_ms of the nearest member may accept
reads. Defaults to 15 milliseconds.

See :class:`~pymongo.read_preferences.ReadPreference`.

.. versionadded:: 2.3

.. note:: ``secondary_acceptable_latency_ms`` is ignored when talking
  to a replica set *through* a mongos. The equivalent is the
  localThreshold_ command line option.

.. _localThreshold: http://docs.mongodb.org/manual/reference/mongos/#cmdoption-mongos--localThreshold
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_read_pref


_BaseObject__get_read_pref
(self)
DocString: The read preference mode for this instance.

See :class:`~pymongo.read_preferences.ReadPreference` for
available options.

.. versionadded:: 2.1
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_safe


_BaseObject__get_safe
(self)
DocString: **DEPRECATED:** Use the 'w' :attr:`write_concern` option instead.

Use getlasterror with every write operation?

.. versionadded:: 2.0
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_slave_okay


_BaseObject__get_slave_okay
(self)
DocString: DEPRECATED. Use :attr:`read_preference` instead.

.. versionchanged:: 2.1
   Deprecated slave_okay.
.. versionadded:: 2.0
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_tag_sets


_BaseObject__get_tag_sets
(self)
DocString: Set ``tag_sets`` to a list of dictionaries like [{'dc': 'ny'}] to
read only from members whose ``dc`` tag has the value ``"ny"``.
To specify a priority-order for tag sets, provide a list of
tag sets: ``[{'dc': 'ny'}, {'dc': 'la'}, {}]``. A final, empty tag
set, ``{}``, means "read from any member that matches the mode,
ignoring tags." ReplicaSetConnection tries each set of tags in turn
until it finds a set of tags with at least one matching member.

   .. seealso:: `Data-Center Awareness
       <http://www.mongodb.org/display/DOCS/Data+Center+Awareness>`_

.. versionadded:: 2.3
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_uuid_subtype


_BaseObject__get_uuid_subtype
(self)
DocString: This attribute specifies which BSON Binary subtype is used when
storing UUIDs. Historically UUIDs have been stored as BSON Binary
subtype 3. This attribute is used to switch to the newer BSON Binary
subtype 4. It can also be used to force legacy byte order and subtype
compatibility with the Java and C# drivers. See the :mod:`bson.binary`
module for all options.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_write_concern


_BaseObject__get_write_concern
(self)
DocString: The default write concern for this instance.

Supports dict style access for getting/setting write concern
options. Valid options include:

- `w`: (integer or string) If this is a replica set, write operations
  will block until they have been replicated to the specified number
  or tagged set of servers. `w=<int>` always includes the replica set
  primary (e.g. w=3 means write to the primary and wait until
  replicated to **two** secondaries). **Setting w=0 disables write
  acknowledgement and all other write concern options.**
- `wtimeout`: (integer) Used in conjunction with `w`. Specify a value
  in milliseconds to control how long to wait for write propagation
  to complete. If replication does not complete in the given
  timeframe, a timeout exception is raised.
- `j`: If ``True`` block until write operations have been committed
  to the journal. Cannot be used in combination with `fsync`. Prior
  to MongoDB 2.6 this option was ignored if the server was running
  without journaling. Starting with MongoDB 2.6 write operations will
  fail with an exception if this option is used when the server is
  running without journaling.
- `fsync`: If ``True`` and the server is running without journaling,
  blocks until the server has synced all data files to disk. If the
  server is running with journaling, this acts the same as the `j`
  option, blocking until write operations have been committed to the
  journal. Cannot be used in combination with `j`.

>>> m = pymongo.MongoClient()
>>> m.write_concern
{}
>>> m.write_concern = {'w': 2, 'wtimeout': 1000}
>>> m.write_concern
{'wtimeout': 1000, 'w': 2}
>>> m.write_concern['j'] = True
>>> m.write_concern
{'wtimeout': 1000, 'j': True, 'w': 2}
>>> m.write_concern = {'j': True}
>>> m.write_concern
{'j': True}
>>> # Disable write acknowledgement and write concern
...
>>> m.write_concern['w'] = 0


.. note:: Accessing :attr:`write_concern` returns its value
   (a subclass of :class:`dict`), not a copy.

.. warning:: If you are using :class:`~pymongo.connection.Connection`
   or :class:`~pymongo.replica_set_connection.ReplicaSetConnection`
   make sure you explicitly set ``w`` to 1 (or a greater value) or
   :attr:`safe` to ``True``. Unlike calling
   :meth:`set_lasterror_options`, setting an option in
   :attr:`write_concern` does not implicitly set :attr:`safe`
   to ``True``.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_acceptable_latency


_BaseObject__set_acceptable_latency
(self, value)
DocString: Property setter for secondary_acceptable_latency_ms
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_options


_BaseObject__set_options
(self, options)
DocString: Validates and sets all options passed to this object.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_read_pref


_BaseObject__set_read_pref
(self, value)
DocString: Property setter for read_preference
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_safe


_BaseObject__set_safe
(self, value)
DocString: Property setter for safe
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_safe_option


_BaseObject__set_safe_option
(self, option, value)
DocString: Validates and sets getlasterror options for this
object (Connection, Database, Collection, etc.)
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_slave_okay


_BaseObject__set_slave_okay
(self, value)
DocString: Property setter for slave_okay
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_tag_sets


_BaseObject__set_tag_sets
(self, value)
DocString: Property setter for tag_sets
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_uuid_subtype


_BaseObject__set_uuid_subtype
(self, value)
DocString: Sets the BSON Binary subtype to be used when storing UUIDs.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_write_concern


_BaseObject__set_write_concern
(self, value)
DocString: Property setter for write_concern.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__check_auth


_MongoReplicaSetClient__check_auth
(self, sock_info)
DocString: Authenticate using cached database credentials.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__check_bson_size


_MongoReplicaSetClient__check_bson_size
(self, msg, max_size)
DocString: Make sure the message doesn't include BSON documents larger
than the connected server will accept.

:Parameters:
  - `msg`: message to check
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__check_response_to_last_error


_MongoReplicaSetClient__check_response_to_last_error
(self, response, is_command)
DocString: Check a response to a lastError message for errors.

`response` is a byte string representing a response to the message.
If it represents an error response we raise OperationFailure.

Return the response as a document.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__create_rs_state


_MongoReplicaSetClient__create_rs_state
(self, rs_state, initial)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__ensure_monitor


_MongoReplicaSetClient__ensure_monitor
(self)
DocString: Ensure the monitor is started, and return it.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__find_primary


_MongoReplicaSetClient__find_primary
(self)
DocString: Returns a connection to the primary of this replica set,
if one exists, or raises AutoReconnect.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__get_rs_state


_MongoReplicaSetClient__get_rs_state
(self)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__is_master


_MongoReplicaSetClient__is_master
(self, host)
DocString: Directly call ismaster.
Returns (response, connection_pool, ping_time in seconds).
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__make_threadlocal


_MongoReplicaSetClient__make_threadlocal
(self)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__recv_data


_MongoReplicaSetClient__recv_data
(self, length, sock_info)
DocString: Lowest level receive operation.

Takes length to receive and repeatedly calls recv until able to
return a buffer of that length, raising ConnectionFailure on error.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__recv_msg


_MongoReplicaSetClient__recv_msg
(self, operation, rqst_id, sock)
DocString: Receive a message in response to `rqst_id` on `sock`.

Returns the response data with the header removed.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__schedule_refresh


_MongoReplicaSetClient__schedule_refresh
(self, sync=False)
DocString: Awake the monitor to update our view of the replica set's state.

If `sync` is True, block until the refresh completes.

If multiple application threads call __schedule_refresh while refresh
is in progress, the work of refreshing the state is only performed
once.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__send_and_receive


_MongoReplicaSetClient__send_and_receive
(self, member, msg, **kwargs)
DocString: Send a message on the given socket and return the response data.

Can raise socket.error.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__simple_command


_MongoReplicaSetClient__simple_command
(self, sock_info, dbname, spec)
DocString: Send a command to the server.
Returns (response, ping_time in seconds).
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__socket


_MongoReplicaSetClient__socket
(self, member, force=False)
DocString: Get a SocketInfo from the pool.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__try_read


_MongoReplicaSetClient__try_read
(self, member, msg, **kwargs)
DocString: Attempt a read from a member; on failure mark the member "down" and
wake up the monitor thread to refresh as soon as possible.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__eq__


__eq__
(self, other)
DocString: Return self==value.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__getattr__


__getattr__
(self, name)
DocString: Get a database by name.

Raises :class:`~pymongo.errors.InvalidName` if an invalid
database name is used.

:Parameters:
  - `name`: the name of the database to get
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__getitem__


__getitem__
(self, name)
DocString: Get a database by name.

Raises :class:`~pymongo.errors.InvalidName` if an invalid
database name is used.

:Parameters:
  - `name`: the name of the database to get
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__init__


__init__
(self, hosts_or_uri=None, max_pool_size=100, document_class=<class 'dict'>, tz_aware=False, _connect=True, **kwargs)
DocString: Create a new connection to a MongoDB replica set.

The resultant client object has connection-pooling built
in. It also performs auto-reconnection when necessary. If an
operation fails because of a connection error,
:class:`~pymongo.errors.ConnectionFailure` is raised. If
auto-reconnection will be performed,
:class:`~pymongo.errors.AutoReconnect` will be
raised. Application code should handle this exception
(recognizing that the operation failed) and then continue to
execute.

Raises :class:`~pymongo.errors.ConnectionFailure` if
the connection cannot be made.

The `hosts_or_uri` parameter can be a full `mongodb URI
<http://dochub.mongodb.org/core/connections>`_, in addition to
a string of `host:port` pairs (e.g. 'host1:port1,host2:port2').
If `hosts_or_uri` is None 'localhost:27017' will be used.

.. note:: Instances of :class:`MongoReplicaSetClient` start a
   background task to monitor the state of the replica set. This allows
   it to quickly respond to changes in replica set configuration.
   Before discarding an instance of :class:`MongoReplicaSetClient` make
   sure you call :meth:`~close` to ensure that the monitor task is
   cleanly shut down.

:Parameters:
  - `hosts_or_uri` (optional): A MongoDB URI or string of `host:port`
    pairs. If a host is an IPv6 literal it must be enclosed in '[' and
    ']' characters following the RFC2732 URL syntax (e.g. '[::1]' for
    localhost)
  - `max_pool_size` (optional): The maximum number of connections
    each pool will open simultaneously. If this is set, operations
    will block if there are `max_pool_size` outstanding connections
    from the pool. Defaults to 100.
  - `document_class` (optional): default class to use for
    documents returned from queries on this client
  - `tz_aware` (optional): if ``True``,
    :class:`~datetime.datetime` instances returned as values
    in a document by this :class:`MongoReplicaSetClient` will be timezone
    aware (otherwise they will be naive)
  - `replicaSet`: (required) The name of the replica set to connect to.
    The driver will verify that each host it connects to is a member of
    this replica set. Can be passed as a keyword argument or as a
    MongoDB URI option.

  | **Other optional parameters can be passed as keyword arguments:**

  - `host`: For compatibility with :class:`~mongo_client.MongoClient`.
    If both `host` and `hosts_or_uri` are specified `host` takes
    precedence.
  - `port`: For compatibility with :class:`~mongo_client.MongoClient`.
    The default port number to use for hosts.
  - `socketTimeoutMS`: (integer or None) How long (in milliseconds) a
    send or receive on a socket can take before timing out. Defaults to
    ``None`` (no timeout).
  - `connectTimeoutMS`: (integer or None) How long (in milliseconds) a
    connection can take to be opened before timing out. Defaults to
    ``20000``.
  - `waitQueueTimeoutMS`: (integer or None) How long (in milliseconds)
    a thread will wait for a socket from the pool if the pool has no
    free sockets. Defaults to ``None`` (no timeout).
  - `waitQueueMultiple`: (integer or None) Multiplied by max_pool_size
    to give the number of threads allowed to wait for a socket at one
    time. Defaults to ``None`` (no waiters).
  - `socketKeepAlive`: (boolean) Whether to send periodic keep-alive
    packets on connected sockets. Defaults to ``False`` (do not send
    keep-alive packets).
  - `auto_start_request`: Deprecated.
  - `use_greenlets`: If ``True``, use a background Greenlet instead of
    a background thread to monitor the state of the replica set.
    Additionally, :meth:`start_request` assigns a greenlet-local,
    rather than thread-local, socket. Defaults to ``False``.
    `use_greenlets` with :class:`MongoReplicaSetClient` requires
    `Gevent <http://gevent.org/>`_ to be installed.

  | **Write Concern options:**
  | (Only set if passed. No default values.)

  - `w`: (integer or string) Write operations will block until they have
    been replicated to the specified number or tagged set of servers.
    `w=<int>` always includes the replica set primary (e.g. w=3 means
    write to the primary and wait until replicated to **two**
    secondaries). Passing w=0 **disables write acknowledgement** and all
    other write concern options.
  - `wtimeout`: (integer) Used in conjunction with `w`. Specify a value
    in milliseconds to control how long to wait for write propagation
    to complete. If replication does not complete in the given
    timeframe, a timeout exception is raised.
  - `j`: If ``True`` block until write operations have been committed
    to the journal. Cannot be used in combination with `fsync`. Prior
    to MongoDB 2.6 this option was ignored if the server was running
    without journaling. Starting with MongoDB 2.6 write operations will
    fail with an exception if this option is used when the server is
    running without journaling.
  - `fsync`: If ``True`` and the server is running without journaling,
    blocks until the server has synced all data files to disk. If the
    server is running with journaling, this acts the same as the `j`
    option, blocking until write operations have been committed to the
    journal. Cannot be used in combination with `j`.

  | **Read preference options:**

  - `read_preference`: The read preference for this client.
    See :class:`~pymongo.read_preferences.ReadPreference` for available
    options. Defaults to ``PRIMARY``.
  - `tag_sets`: Read from replica-set members with these tags.
    To specify a priority-order for tag sets, provide a list of
    tag sets: ``[{'dc': 'ny'}, {'dc': 'la'}, {}]``. A final, empty tag
    set, ``{}``, means "read from any member that matches the mode,
    ignoring tags." :class:`MongoReplicaSetClient` tries each set of
    tags in turn until it finds a set of tags with at least one matching
    member. Defaults to ``[{}]``, meaning "ignore members' tags."
  - `secondary_acceptable_latency_ms`: (integer) Any replica-set member
    whose ping time is within secondary_acceptable_latency_ms of the
    nearest member may accept reads. Default 15 milliseconds.
    **Ignored by mongos** and must be configured on the command line.
    See the localThreshold_ option for more information.

  | **SSL configuration:**

  - `ssl`: If ``True``, create the connection to the servers using SSL.
    Defaults to ``False``.
  - `ssl_keyfile`: The private keyfile used to identify the local
    connection against mongod.  If included with the ``certfile`` then
    only the ``ssl_certfile`` is needed.  Implies ``ssl=True``.
    Defaults to ``None``.
  - `ssl_certfile`: The certificate file used to identify the local
    connection against mongod. Implies ``ssl=True``. Defaults to
    ``None``.
  - `ssl_cert_reqs`: Specifies whether a certificate is required from
    the other side of the connection, and whether it will be validated
    if provided. It must be one of the three values ``ssl.CERT_NONE``
    (certificates ignored), ``ssl.CERT_OPTIONAL``
    (not required, but validated if provided), or ``ssl.CERT_REQUIRED``
    (required and validated). If the value of this parameter is not
    ``ssl.CERT_NONE``, then the ``ssl_ca_certs`` parameter must point
    to a file of CA certificates. Implies ``ssl=True``. Defaults to
    ``ssl.CERT_NONE``.
  - `ssl_ca_certs`: The ca_certs file contains a set of concatenated
    "certification authority" certificates, which are used to validate
    certificates passed from the other end of the connection.
    Implies ``ssl=True``. Defaults to ``None``.

.. versionchanged:: 2.5
   Added additional ssl options
.. versionadded:: 2.4

.. _localThreshold: http://docs.mongodb.org/manual/reference/mongos/#cmdoption-mongos--localThreshold
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__ne__


__ne__
(self, other)
DocString: Return self!=value.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__repr__


__repr__
(self)
DocString: Return repr(self).
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_cache_credentials


_cache_credentials
(self, source, credentials, connect=True)
DocString: Add credentials to the database authentication cache
for automatic login when a socket is created. If `connect` is True,
verify the credentials on the server first.

Raises OperationFailure if other credentials are already stored for
this source.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_cache_index


_cache_index
(self, dbase, collection, index, cache_for)
DocString: Add an index to the index cache for ensure_index operations.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_cached


_cached
(self, dbname, coll, index)
DocString: Test if `index` is cached.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_ensure_connected


_ensure_connected
(self, sync=False)
DocString: Ensure this client instance is connected to a primary.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_exhaust_next


_exhaust_next
(self, sock_info)
DocString: Used with exhaust cursors to get the next batch off the socket.

Can raise AutoReconnect.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_get_wc_override


_get_wc_override
(self)
DocString: Get write concern override.

Used in internal methods that **must** do acknowledged write ops.
We don't want to override user write concern options if write concern
is already enabled.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_get_write_mode


_get_write_mode
(self, safe=None, **options)
DocString: Get the current write mode.

Determines if the current write is safe or not based on the
passed in or inherited safe value, write_concern values, or
passed options.

:Parameters:
    - `safe`: check that the operation succeeded?
    - `**options`: overriding write concern options.

.. versionadded:: 2.3
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_purge_credentials


_purge_credentials
(self, source)
DocString: Purge credentials from the database authentication cache.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_purge_index


_purge_index
(self, database_name, collection_name=None, index_name=None)
DocString: Purge an index from the index cache.

If `index_name` is None purge an entire collection.

If `collection_name` is None purge an entire database.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_send_message


_send_message
(self, msg, with_last_error=False, command=False, _connection_to_use=None)
DocString: Say something to Mongo.

Raises ConnectionFailure if the message cannot be sent. Raises
OperationFailure if `with_last_error` is ``True`` and the
response to the getLastError call returns an error. Return the
response from lastError, or ``None`` if `with_last_error` is
``False``.

:Parameters:
  - `msg`: message to send
  - `with_last_error`: check getLastError status after sending the
    message
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_send_message_with_response


_send_message_with_response
(self, msg, _connection_to_use=None, _must_use_master=False, **kwargs)
DocString: Send a message to Mongo and return the response.

Sends the given message and returns (host used, response).

:Parameters:
  - `msg`: (request_id, data) pair making up the message to send
  - `_connection_to_use`: Optional (host, port) of member for message,
    used by Cursor for getMore and killCursors messages.
  - `_must_use_master`: If True, send to primary.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
alive


alive
(self)
DocString: Return ``False`` if there has been an error communicating with the
primary, else ``True``.

This method attempts to check the status of the primary with minimal
I/O. The current thread / greenlet retrieves a socket from the
primary's connection pool and checks whether calling select_ on it
raises an error. If there are currently no idle sockets,
:meth:`alive` attempts to connect a new socket.

A more certain way to determine primary availability is to ping it::

    client.admin.command('ping')

.. _select: http://docs.python.org/2/library/select.html#select.select
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
close


close
(self)
DocString: Close this client instance.

This method first terminates the replica set monitor, then disconnects
from all members of the replica set. No further operations are
permitted on this client.

.. warning:: This method stops the replica set monitor task. The
   replica set monitor is required to properly handle replica set
   configuration changes, including a failure of the primary.
   Once :meth:`~close` is called this client instance must not be
   reused.

.. versionchanged:: 2.2.1
   The :meth:`close` method now terminates the replica set monitor.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
close_cursor


close_cursor
(self, cursor_id, _conn_id)
DocString: Close a single database cursor.

Raises :class:`TypeError` if `cursor_id` is not an instance of
``(int, long)``.

:Parameters:
  - `cursor_id`: id of cursor to close
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
copy_database


copy_database
(self, from_name, to_name, from_host=None, username=None, password=None, mechanism='DEFAULT')
DocString: **DEPRECATED**: Copy a database, potentially from another host.

:meth:`copy_database` will be removed in PyMongo 3.0. See the
:doc:`copy_database examples </examples/copydb>` for alternatives.

Raises :class:`TypeError` if `from_name` or `to_name` is not
an instance of :class:`basestring` (:class:`str` in python 3).
Raises :class:`~pymongo.errors.InvalidName` if `to_name` is
not a valid database name.

If `from_host` is ``None`` the current host is used as the
source. Otherwise the database is copied from `from_host`.

If the source database requires authentication, `username` and
`password` must be specified. By default, use SCRAM-SHA-1 with
MongoDB 3.0 and later, MONGODB-CR (MongoDB Challenge Response
protocol) for older servers.

:Parameters:
  - `from_name`: the name of the source database
  - `to_name`: the name of the target database
  - `from_host` (optional): host name to copy from
  - `username` (optional): username for source database
  - `password` (optional): password for source database
  - `mechanism` (optional): auth method, 'MONGODB-CR' or 'SCRAM-SHA-1'

.. seealso:: The :doc:`copy_database examples </examples/copydb>`.

.. versionchanged:: 2.8
   Deprecated copy_database, and added SCRAM-SHA-1 support.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
database_names


database_names
(self)
DocString: Get a list of the names of all databases on the connected server.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
disconnect


disconnect
(self)
DocString: Disconnect from the replica set primary, unpin all members, and
refresh our view of the replica set.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
drop_database


drop_database
(self, name_or_database)
DocString: Drop a database.

Raises :class:`TypeError` if `name_or_database` is not an instance of
:class:`basestring` (:class:`str` in python 3) or Database

:Parameters:
  - `name_or_database`: the name of a database to drop, or a
    :class:`~pymongo.database.Database` instance representing the
    database to drop
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
end_request


end_request
(self)
DocString: **DEPRECATED**: Undo :meth:`start_request`.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
get_default_database


get_default_database
(self)
DocString: Get the database named in the MongoDB connection URI.

>>> uri = 'mongodb://host/my_database'
>>> client = MongoReplicaSetClient(uri)
>>> db = client.get_default_database()
>>> assert db.name == 'my_database'

Useful in scripts where you want to choose which database to use
based only on the URI in a configuration file.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
get_document_class


get_document_class
(self)
DocString: document_class getter
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
get_lasterror_options


get_lasterror_options
(self)
DocString: DEPRECATED: Use :attr:`write_concern` instead.

Returns a dict of the getlasterror options set on this instance.

.. versionchanged:: 2.4
   Deprecated get_lasterror_options.
.. versionadded:: 2.0
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
in_request


in_request
(self)
DocString: **DEPRECATED**: True if :meth:`start_request` has been called, but
not :meth:`end_request`, or if `auto_start_request` is True and
:meth:`end_request` has not been called in this thread or greenlet.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
refresh


refresh
(self, initial=False)
DocString: Iterate through the existing host list, or possibly the
seed list, to update the list of hosts and arbiters in this
replica set.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
server_info


server_info
(self)
DocString: Get information about the MongoDB primary we're connected to.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
set_document_class


set_document_class
(self, klass)
DocString: document_class setter
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
set_lasterror_options


set_lasterror_options
(self, **kwargs)
DocString: DEPRECATED: Use :attr:`write_concern` instead.

Set getlasterror options for this instance.

Valid options include j=<bool>, w=<int/string>, wtimeout=<int>,
and fsync=<bool>. Implies safe=True.

:Parameters:
    - `**kwargs`: Options should be passed as keyword
                  arguments (e.g. w=2, fsync=True)

.. versionchanged:: 2.4
   Deprecated set_lasterror_options.
.. versionadded:: 2.0
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
start_request


start_request
(self)
DocString: **DEPRECATED**: start_request will be removed in PyMongo 3.0.

When doing w=0 writes to MongoDB 2.4 or earlier, :meth:`start_request`
was sometimes useful to ensure the current thread always used the same
socket until it called :meth:`end_request`. This made consistent reads
more likely after an unacknowledged write. Requests are no longer
useful in modern MongoDB applications, see
`PYTHON-785 <https://jira.mongodb.org/browse/PYTHON-785>`_.

.. versionchanged:: 2.8
   Deprecated.

.. versionadded:: 2.2
   The :class:`~pymongo.pool.Request` return value.
   :meth:`start_request` previously returned None
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
unset_lasterror_options


unset_lasterror_options
(self, *options)
DocString: DEPRECATED: Use :attr:`write_concern` instead.

Unset getlasterror options for this instance.

If no options are passed unsets all getlasterror options.
This does not set `safe` to False.

:Parameters:
    - `*options`: The list of options to unset.

.. versionchanged:: 2.4
   Deprecated unset_lasterror_options.
.. versionadded:: 2.0
####################################################################################################
ReadPreference
An enum that defines the read preference modes supported by PyMongo.
Used in three cases:

:class:`~pymongo.mongo_client.MongoClient` connected to a single host:

* `PRIMARY`: Queries are allowed if the host is standalone or the replica
  set primary.
* All other modes allow queries to standalone servers, to the primary, or
  to secondaries.

:class:`~pymongo.mongo_client.MongoClient` connected to a mongos, with a
sharded cluster of replica sets:

* `PRIMARY`: Queries are sent to the primary of a shard.
* `PRIMARY_PREFERRED`: Queries are sent to the primary if available,
  otherwise a secondary.
* `SECONDARY`: Queries are distributed among shard secondaries. An error
  is raised if no secondaries are available.
* `SECONDARY_PREFERRED`: Queries are distributed among shard secondaries,
  or the primary if no secondary is available.
* `NEAREST`: Queries are distributed among all members of a shard.

:class:`~pymongo.mongo_replica_set_client.MongoReplicaSetClient`:

* `PRIMARY`: Queries are sent to the primary of the replica set.
* `PRIMARY_PREFERRED`: Queries are sent to the primary if available,
  otherwise a secondary.
* `SECONDARY`: Queries are distributed among secondaries. An error
  is raised if no secondaries are available.
* `SECONDARY_PREFERRED`: Queries are distributed among secondaries,
  or the primary if no secondary is available.
* `NEAREST`: Queries are distributed among all members.
####################################################################################################
ReplicaSetConnection
Connection to a MongoDB replica set.
    
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_acceptable_latency


_BaseObject__get_acceptable_latency
(self)
DocString: Any replica-set member whose ping time is within
secondary_acceptable_latency_ms of the nearest member may accept
reads. Defaults to 15 milliseconds.

See :class:`~pymongo.read_preferences.ReadPreference`.

.. versionadded:: 2.3

.. note:: ``secondary_acceptable_latency_ms`` is ignored when talking
  to a replica set *through* a mongos. The equivalent is the
  localThreshold_ command line option.

.. _localThreshold: http://docs.mongodb.org/manual/reference/mongos/#cmdoption-mongos--localThreshold
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_read_pref


_BaseObject__get_read_pref
(self)
DocString: The read preference mode for this instance.

See :class:`~pymongo.read_preferences.ReadPreference` for
available options.

.. versionadded:: 2.1
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_safe


_BaseObject__get_safe
(self)
DocString: **DEPRECATED:** Use the 'w' :attr:`write_concern` option instead.

Use getlasterror with every write operation?

.. versionadded:: 2.0
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_slave_okay


_BaseObject__get_slave_okay
(self)
DocString: DEPRECATED. Use :attr:`read_preference` instead.

.. versionchanged:: 2.1
   Deprecated slave_okay.
.. versionadded:: 2.0
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_tag_sets


_BaseObject__get_tag_sets
(self)
DocString: Set ``tag_sets`` to a list of dictionaries like [{'dc': 'ny'}] to
read only from members whose ``dc`` tag has the value ``"ny"``.
To specify a priority-order for tag sets, provide a list of
tag sets: ``[{'dc': 'ny'}, {'dc': 'la'}, {}]``. A final, empty tag
set, ``{}``, means "read from any member that matches the mode,
ignoring tags." ReplicaSetConnection tries each set of tags in turn
until it finds a set of tags with at least one matching member.

   .. seealso:: `Data-Center Awareness
       <http://www.mongodb.org/display/DOCS/Data+Center+Awareness>`_

.. versionadded:: 2.3
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_uuid_subtype


_BaseObject__get_uuid_subtype
(self)
DocString: This attribute specifies which BSON Binary subtype is used when
storing UUIDs. Historically UUIDs have been stored as BSON Binary
subtype 3. This attribute is used to switch to the newer BSON Binary
subtype 4. It can also be used to force legacy byte order and subtype
compatibility with the Java and C# drivers. See the :mod:`bson.binary`
module for all options.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__get_write_concern


_BaseObject__get_write_concern
(self)
DocString: The default write concern for this instance.

Supports dict style access for getting/setting write concern
options. Valid options include:

- `w`: (integer or string) If this is a replica set, write operations
  will block until they have been replicated to the specified number
  or tagged set of servers. `w=<int>` always includes the replica set
  primary (e.g. w=3 means write to the primary and wait until
  replicated to **two** secondaries). **Setting w=0 disables write
  acknowledgement and all other write concern options.**
- `wtimeout`: (integer) Used in conjunction with `w`. Specify a value
  in milliseconds to control how long to wait for write propagation
  to complete. If replication does not complete in the given
  timeframe, a timeout exception is raised.
- `j`: If ``True`` block until write operations have been committed
  to the journal. Cannot be used in combination with `fsync`. Prior
  to MongoDB 2.6 this option was ignored if the server was running
  without journaling. Starting with MongoDB 2.6 write operations will
  fail with an exception if this option is used when the server is
  running without journaling.
- `fsync`: If ``True`` and the server is running without journaling,
  blocks until the server has synced all data files to disk. If the
  server is running with journaling, this acts the same as the `j`
  option, blocking until write operations have been committed to the
  journal. Cannot be used in combination with `j`.

>>> m = pymongo.MongoClient()
>>> m.write_concern
{}
>>> m.write_concern = {'w': 2, 'wtimeout': 1000}
>>> m.write_concern
{'wtimeout': 1000, 'w': 2}
>>> m.write_concern['j'] = True
>>> m.write_concern
{'wtimeout': 1000, 'j': True, 'w': 2}
>>> m.write_concern = {'j': True}
>>> m.write_concern
{'j': True}
>>> # Disable write acknowledgement and write concern
...
>>> m.write_concern['w'] = 0


.. note:: Accessing :attr:`write_concern` returns its value
   (a subclass of :class:`dict`), not a copy.

.. warning:: If you are using :class:`~pymongo.connection.Connection`
   or :class:`~pymongo.replica_set_connection.ReplicaSetConnection`
   make sure you explicitly set ``w`` to 1 (or a greater value) or
   :attr:`safe` to ``True``. Unlike calling
   :meth:`set_lasterror_options`, setting an option in
   :attr:`write_concern` does not implicitly set :attr:`safe`
   to ``True``.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_acceptable_latency


_BaseObject__set_acceptable_latency
(self, value)
DocString: Property setter for secondary_acceptable_latency_ms
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_options


_BaseObject__set_options
(self, options)
DocString: Validates and sets all options passed to this object.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_read_pref


_BaseObject__set_read_pref
(self, value)
DocString: Property setter for read_preference
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_safe


_BaseObject__set_safe
(self, value)
DocString: Property setter for safe
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_safe_option


_BaseObject__set_safe_option
(self, option, value)
DocString: Validates and sets getlasterror options for this
object (Connection, Database, Collection, etc.)
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_slave_okay


_BaseObject__set_slave_okay
(self, value)
DocString: Property setter for slave_okay
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_tag_sets


_BaseObject__set_tag_sets
(self, value)
DocString: Property setter for tag_sets
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_uuid_subtype


_BaseObject__set_uuid_subtype
(self, value)
DocString: Sets the BSON Binary subtype to be used when storing UUIDs.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_BaseObject__set_write_concern


_BaseObject__set_write_concern
(self, value)
DocString: Property setter for write_concern.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__check_auth


_MongoReplicaSetClient__check_auth
(self, sock_info)
DocString: Authenticate using cached database credentials.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__check_bson_size


_MongoReplicaSetClient__check_bson_size
(self, msg, max_size)
DocString: Make sure the message doesn't include BSON documents larger
than the connected server will accept.

:Parameters:
  - `msg`: message to check
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__check_response_to_last_error


_MongoReplicaSetClient__check_response_to_last_error
(self, response, is_command)
DocString: Check a response to a lastError message for errors.

`response` is a byte string representing a response to the message.
If it represents an error response we raise OperationFailure.

Return the response as a document.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__create_rs_state


_MongoReplicaSetClient__create_rs_state
(self, rs_state, initial)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__ensure_monitor


_MongoReplicaSetClient__ensure_monitor
(self)
DocString: Ensure the monitor is started, and return it.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__find_primary


_MongoReplicaSetClient__find_primary
(self)
DocString: Returns a connection to the primary of this replica set,
if one exists, or raises AutoReconnect.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__get_rs_state


_MongoReplicaSetClient__get_rs_state
(self)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__is_master


_MongoReplicaSetClient__is_master
(self, host)
DocString: Directly call ismaster.
Returns (response, connection_pool, ping_time in seconds).
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__make_threadlocal


_MongoReplicaSetClient__make_threadlocal
(self)
No docstring.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__recv_data


_MongoReplicaSetClient__recv_data
(self, length, sock_info)
DocString: Lowest level receive operation.

Takes length to receive and repeatedly calls recv until able to
return a buffer of that length, raising ConnectionFailure on error.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__recv_msg


_MongoReplicaSetClient__recv_msg
(self, operation, rqst_id, sock)
DocString: Receive a message in response to `rqst_id` on `sock`.

Returns the response data with the header removed.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__schedule_refresh


_MongoReplicaSetClient__schedule_refresh
(self, sync=False)
DocString: Awake the monitor to update our view of the replica set's state.

If `sync` is True, block until the refresh completes.

If multiple application threads call __schedule_refresh while refresh
is in progress, the work of refreshing the state is only performed
once.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__send_and_receive


_MongoReplicaSetClient__send_and_receive
(self, member, msg, **kwargs)
DocString: Send a message on the given socket and return the response data.

Can raise socket.error.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__simple_command


_MongoReplicaSetClient__simple_command
(self, sock_info, dbname, spec)
DocString: Send a command to the server.
Returns (response, ping_time in seconds).
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__socket


_MongoReplicaSetClient__socket
(self, member, force=False)
DocString: Get a SocketInfo from the pool.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_MongoReplicaSetClient__try_read


_MongoReplicaSetClient__try_read
(self, member, msg, **kwargs)
DocString: Attempt a read from a member; on failure mark the member "down" and
wake up the monitor thread to refresh as soon as possible.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__eq__


__eq__
(self, other)
DocString: Return self==value.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__getattr__


__getattr__
(self, name)
DocString: Get a database by name.

Raises :class:`~pymongo.errors.InvalidName` if an invalid
database name is used.

:Parameters:
  - `name`: the name of the database to get
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__getitem__


__getitem__
(self, name)
DocString: Get a database by name.

Raises :class:`~pymongo.errors.InvalidName` if an invalid
database name is used.

:Parameters:
  - `name`: the name of the database to get
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__init__


__init__
(self, hosts_or_uri=None, max_pool_size=None, document_class=<class 'dict'>, tz_aware=False, **kwargs)
DocString: Create a new connection to a MongoDB replica set.

.. warning::
   **DEPRECATED:** :class:`ReplicaSetConnection` is deprecated. Please
   use :class:`~pymongo.mongo_replica_set_client.MongoReplicaSetClient`
   instead

The resultant connection object has connection-pooling built
in. It also performs auto-reconnection when necessary. If an
operation fails because of a connection error,
:class:`~pymongo.errors.ConnectionFailure` is raised. If
auto-reconnection will be performed,
:class:`~pymongo.errors.AutoReconnect` will be
raised. Application code should handle this exception
(recognizing that the operation failed) and then continue to
execute.

Raises :class:`~pymongo.errors.ConnectionFailure` if
the connection cannot be made.

The `hosts_or_uri` parameter can be a full `mongodb URI
<http://dochub.mongodb.org/core/connections>`_, in addition to
a string of `host:port` pairs (e.g. 'host1:port1,host2:port2').
If `hosts_or_uri` is None 'localhost:27017' will be used.

.. note:: Instances of :class:`~ReplicaSetConnection` start a
   background task to monitor the state of the replica set. This allows
   it to quickly respond to changes in replica set configuration.
   Before discarding an instance of :class:`~ReplicaSetConnection` make
   sure you call :meth:`~close` to ensure that the monitor task is
   cleanly shut down.

:Parameters:
  - `hosts_or_uri` (optional): A MongoDB URI or string of `host:port`
    pairs. If a host is an IPv6 literal it must be enclosed in '[' and
    ']' characters following the RFC2732 URL syntax (e.g. '[::1]' for
    localhost)
  - `max_pool_size` (optional): The maximum number of connections
    each pool will open simultaneously. If this is set, operations
    will block if there are `max_pool_size` outstanding connections
    from the pool. By default the pool size is unlimited.
  - `document_class` (optional): default class to use for
    documents returned from queries on this connection
  - `tz_aware` (optional): if ``True``,
    :class:`~datetime.datetime` instances returned as values
    in a document by this :class:`ReplicaSetConnection` will be timezone
    aware (otherwise they will be naive)
  - `replicaSet`: (required) The name of the replica set to connect to.
    The driver will verify that each host it connects to is a member of
    this replica set. Can be passed as a keyword argument or as a
    MongoDB URI option.

  | **Other optional parameters can be passed as keyword arguments:**

  - `host`: For compatibility with connection.Connection. If both
    `host` and `hosts_or_uri` are specified `host` takes precedence.
  - `port`: For compatibility with connection.Connection. The default
    port number to use for hosts.
  - `network_timeout`: For compatibility with connection.Connection.
    The timeout (in seconds) to use for socket operations - default
    is no timeout. If both `network_timeout` and `socketTimeoutMS` are
    specified `network_timeout` takes precedence, matching
    connection.Connection.
  - `socketTimeoutMS`: (integer or None) How long (in milliseconds) a
    send or receive on a socket can take before timing out. Defaults
    to ``None`` (no timeout).
  - `connectTimeoutMS`: (integer or None) How long (in milliseconds) a
    connection can take to be opened before timing out. Defaults to
    ``20000``.
  - `waitQueueTimeoutMS`: (integer or None) How long (in milliseconds)
    a thread will wait for a socket from the pool if the pool has no
    free sockets. Defaults to ``None`` (no timeout).
  - `waitQueueMultiple`: (integer or None) Multiplied by max_pool_size
    to give the number of threads allowed to wait for a socket at one
    time. Defaults to ``None`` (no waiters).
  - `socketKeepAlive`: (boolean) Whether to send periodic keep-alive
    packets on connected sockets. Defaults to ``False`` (do not send
    keep-alive packets).
  - `auto_start_request`: If ``True`` (the default), each thread that
    accesses this :class:`ReplicaSetConnection` has a socket allocated
    to it for each member of the set until the thread calls
    :meth:`end_request` or terminates.
  - `use_greenlets`: if ``True``, use a background Greenlet instead of
    a background thread to monitor state of replica set. Additionally,
    :meth:`start_request()` will ensure that the current greenlet uses
    the same socket for all operations until :meth:`end_request()`.
    Defaults to ``False``.
    `use_greenlets` with ReplicaSetConnection requires `Gevent
    <http://gevent.org/>`_ to be installed.

  | **Write Concern options:**

  - `safe`: :class:`ReplicaSetConnection` **disables** acknowledgement
    of write operations. Use ``safe=True`` to enable write
    acknowledgement.
  - `w`: (integer or string) Write operations will block until they have
    been replicated to the specified number or tagged set of servers.
    `w=<int>` always includes the replica set primary (e.g. w=3 means
    write to the primary and wait until replicated to **two**
    secondaries). Implies safe=True.
  - `wtimeout`: (integer) Used in conjunction with `w`. Specify a value
    in milliseconds to control how long to wait for write propagation
    to complete. If replication does not complete in the given
    timeframe, a timeout exception is raised. Implies safe=True.
  - `j`: If ``True`` block until write operations have been committed
    to the journal. Cannot be used in combination with `fsync`. Prior
    to MongoDB 2.6 this option was ignored if the server was running
    without journaling. Starting with MongoDB 2.6 write operations will
    fail with an exception if this option is used when the server is
    running without journaling. Implies safe=True.
  - `fsync`: If ``True`` and the server is running without journaling,
    blocks until the server has synced all data files to disk. If the
    server is running with journaling, this acts the same as the `j`
    option, blocking until write operations have been committed to the
    journal. Cannot be used in combination with `j`. Implies safe=True.

  | **Read preference options:**

  - `slave_okay` or `slaveOk` (deprecated): Use `read_preference`
    instead.
  - `read_preference`: The read preference for this connection.
    See :class:`~pymongo.read_preferences.ReadPreference` for available
    options. Defaults to ``PRIMARY``.
  - `tag_sets`: Read from replica-set members with these tags.
    To specify a priority-order for tag sets, provide a list of
    tag sets: ``[{'dc': 'ny'}, {'dc': 'la'}, {}]``. A final, empty tag
    set, ``{}``, means "read from any member that matches the mode,
    ignoring tags." :class:`MongoReplicaSetClient` tries each set of
    tags in turn until it finds a set of tags with at least one matching
    member. Defaults to ``[{}]``, meaning "ignore members' tags."
  - `secondary_acceptable_latency_ms`: (integer) Any replica-set member
    whose ping time is within secondary_acceptable_latency_ms of the
    nearest member may accept reads. Default 15 milliseconds.
    **Ignored by mongos** and must be configured on the command line.
    See the localThreshold_ option for more information.

  | **SSL configuration:**

  - `ssl`: If ``True``, create the connection to the servers using SSL.
    Defaults to ``False``.
  - `ssl_keyfile`: The private keyfile used to identify the local
    connection against mongod.  If included with the ``certfile` then
    only the ``ssl_certfile`` is needed.  Implies ``ssl=True``.
    Defaults to ``None``.
  - `ssl_certfile`: The certificate file used to identify the local
    connection against mongod. Implies ``ssl=True``. Defaults to
    ``None``.
  - `ssl_cert_reqs`: Specifies whether a certificate is required from
    the other side of the connection, and whether it will be validated
    if provided. It must be one of the three values ``ssl.CERT_NONE``
    (certificates ignored), ``ssl.CERT_OPTIONAL``
    (not required, but validated if provided), or ``ssl.CERT_REQUIRED``
    (required and validated). If the value of this parameter is not
    ``ssl.CERT_NONE``, then the ``ssl_ca_certs`` parameter must point
    to a file of CA certificates. Implies ``ssl=True``. Defaults to
    ``ssl.CERT_NONE``.
  - `ssl_ca_certs`: The ca_certs file contains a set of concatenated
    "certification authority" certificates, which are used to validate
    certificates passed from the other end of the connection.
    Implies ``ssl=True``. Defaults to ``None``.

.. versionchanged:: 2.5
   Added additional ssl options
.. versionchanged:: 2.3
   Added `tag_sets` and `secondary_acceptable_latency_ms` options.
.. versionchanged:: 2.2
   Added `auto_start_request` and `use_greenlets` options.
   Added support for `host`, `port`, and `network_timeout` keyword
   arguments for compatibility with connection.Connection.
.. versionadded:: 2.1

.. _localThreshold: http://docs.mongodb.org/manual/reference/mongos/#cmdoption-mongos--localThreshold
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__ne__


__ne__
(self, other)
DocString: Return self!=value.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__repr__


__repr__
(self)
DocString: Return repr(self).
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_cache_credentials


_cache_credentials
(self, source, credentials, connect=True)
DocString: Add credentials to the database authentication cache
for automatic login when a socket is created. If `connect` is True,
verify the credentials on the server first.

Raises OperationFailure if other credentials are already stored for
this source.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_cache_index


_cache_index
(self, dbase, collection, index, cache_for)
DocString: Add an index to the index cache for ensure_index operations.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_cached


_cached
(self, dbname, coll, index)
DocString: Test if `index` is cached.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_ensure_connected


_ensure_connected
(self, sync=False)
DocString: Ensure this client instance is connected to a primary.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_exhaust_next


_exhaust_next
(self, sock_info)
DocString: Used with exhaust cursors to get the next batch off the socket.

Can raise AutoReconnect.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_get_wc_override


_get_wc_override
(self)
DocString: Get write concern override.

Used in internal methods that **must** do acknowledged write ops.
We don't want to override user write concern options if write concern
is already enabled.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_get_write_mode


_get_write_mode
(self, safe=None, **options)
DocString: Get the current write mode.

Determines if the current write is safe or not based on the
passed in or inherited safe value, write_concern values, or
passed options.

:Parameters:
    - `safe`: check that the operation succeeded?
    - `**options`: overriding write concern options.

.. versionadded:: 2.3
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_purge_credentials


_purge_credentials
(self, source)
DocString: Purge credentials from the database authentication cache.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_purge_index


_purge_index
(self, database_name, collection_name=None, index_name=None)
DocString: Purge an index from the index cache.

If `index_name` is None purge an entire collection.

If `collection_name` is None purge an entire database.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_send_message


_send_message
(self, msg, with_last_error=False, command=False, _connection_to_use=None)
DocString: Say something to Mongo.

Raises ConnectionFailure if the message cannot be sent. Raises
OperationFailure if `with_last_error` is ``True`` and the
response to the getLastError call returns an error. Return the
response from lastError, or ``None`` if `with_last_error` is
``False``.

:Parameters:
  - `msg`: message to send
  - `with_last_error`: check getLastError status after sending the
    message
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
_send_message_with_response


_send_message_with_response
(self, msg, _connection_to_use=None, _must_use_master=False, **kwargs)
DocString: Send a message to Mongo and return the response.

Sends the given message and returns (host used, response).

:Parameters:
  - `msg`: (request_id, data) pair making up the message to send
  - `_connection_to_use`: Optional (host, port) of member for message,
    used by Cursor for getMore and killCursors messages.
  - `_must_use_master`: If True, send to primary.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
alive


alive
(self)
DocString: Return ``False`` if there has been an error communicating with the
primary, else ``True``.

This method attempts to check the status of the primary with minimal
I/O. The current thread / greenlet retrieves a socket from the
primary's connection pool and checks whether calling select_ on it
raises an error. If there are currently no idle sockets,
:meth:`alive` attempts to connect a new socket.

A more certain way to determine primary availability is to ping it::

    client.admin.command('ping')

.. _select: http://docs.python.org/2/library/select.html#select.select
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
close


close
(self)
DocString: Close this client instance.

This method first terminates the replica set monitor, then disconnects
from all members of the replica set. No further operations are
permitted on this client.

.. warning:: This method stops the replica set monitor task. The
   replica set monitor is required to properly handle replica set
   configuration changes, including a failure of the primary.
   Once :meth:`~close` is called this client instance must not be
   reused.

.. versionchanged:: 2.2.1
   The :meth:`close` method now terminates the replica set monitor.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
close_cursor


close_cursor
(self, cursor_id, _conn_id)
DocString: Close a single database cursor.

Raises :class:`TypeError` if `cursor_id` is not an instance of
``(int, long)``.

:Parameters:
  - `cursor_id`: id of cursor to close
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
copy_database


copy_database
(self, from_name, to_name, from_host=None, username=None, password=None, mechanism='DEFAULT')
DocString: **DEPRECATED**: Copy a database, potentially from another host.

:meth:`copy_database` will be removed in PyMongo 3.0. See the
:doc:`copy_database examples </examples/copydb>` for alternatives.

Raises :class:`TypeError` if `from_name` or `to_name` is not
an instance of :class:`basestring` (:class:`str` in python 3).
Raises :class:`~pymongo.errors.InvalidName` if `to_name` is
not a valid database name.

If `from_host` is ``None`` the current host is used as the
source. Otherwise the database is copied from `from_host`.

If the source database requires authentication, `username` and
`password` must be specified. By default, use SCRAM-SHA-1 with
MongoDB 3.0 and later, MONGODB-CR (MongoDB Challenge Response
protocol) for older servers.

:Parameters:
  - `from_name`: the name of the source database
  - `to_name`: the name of the target database
  - `from_host` (optional): host name to copy from
  - `username` (optional): username for source database
  - `password` (optional): password for source database
  - `mechanism` (optional): auth method, 'MONGODB-CR' or 'SCRAM-SHA-1'

.. seealso:: The :doc:`copy_database examples </examples/copydb>`.

.. versionchanged:: 2.8
   Deprecated copy_database, and added SCRAM-SHA-1 support.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
database_names


database_names
(self)
DocString: Get a list of the names of all databases on the connected server.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
disconnect


disconnect
(self)
DocString: Disconnect from the replica set primary, unpin all members, and
refresh our view of the replica set.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
drop_database


drop_database
(self, name_or_database)
DocString: Drop a database.

Raises :class:`TypeError` if `name_or_database` is not an instance of
:class:`basestring` (:class:`str` in python 3) or Database

:Parameters:
  - `name_or_database`: the name of a database to drop, or a
    :class:`~pymongo.database.Database` instance representing the
    database to drop
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
end_request


end_request
(self)
DocString: **DEPRECATED**: Undo :meth:`start_request`.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
get_default_database


get_default_database
(self)
DocString: Get the database named in the MongoDB connection URI.

>>> uri = 'mongodb://host/my_database'
>>> client = MongoReplicaSetClient(uri)
>>> db = client.get_default_database()
>>> assert db.name == 'my_database'

Useful in scripts where you want to choose which database to use
based only on the URI in a configuration file.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
get_document_class


get_document_class
(self)
DocString: document_class getter
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
get_lasterror_options


get_lasterror_options
(self)
DocString: DEPRECATED: Use :attr:`write_concern` instead.

Returns a dict of the getlasterror options set on this instance.

.. versionchanged:: 2.4
   Deprecated get_lasterror_options.
.. versionadded:: 2.0
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
in_request


in_request
(self)
DocString: **DEPRECATED**: True if :meth:`start_request` has been called, but
not :meth:`end_request`, or if `auto_start_request` is True and
:meth:`end_request` has not been called in this thread or greenlet.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
refresh


refresh
(self, initial=False)
DocString: Iterate through the existing host list, or possibly the
seed list, to update the list of hosts and arbiters in this
replica set.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
server_info


server_info
(self)
DocString: Get information about the MongoDB primary we're connected to.
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
set_document_class


set_document_class
(self, klass)
DocString: document_class setter
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
set_lasterror_options


set_lasterror_options
(self, **kwargs)
DocString: DEPRECATED: Use :attr:`write_concern` instead.

Set getlasterror options for this instance.

Valid options include j=<bool>, w=<int/string>, wtimeout=<int>,
and fsync=<bool>. Implies safe=True.

:Parameters:
    - `**kwargs`: Options should be passed as keyword
                  arguments (e.g. w=2, fsync=True)

.. versionchanged:: 2.4
   Deprecated set_lasterror_options.
.. versionadded:: 2.0
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
start_request


start_request
(self)
DocString: **DEPRECATED**: start_request will be removed in PyMongo 3.0.

When doing w=0 writes to MongoDB 2.4 or earlier, :meth:`start_request`
was sometimes useful to ensure the current thread always used the same
socket until it called :meth:`end_request`. This made consistent reads
more likely after an unacknowledged write. Requests are no longer
useful in modern MongoDB applications, see
`PYTHON-785 <https://jira.mongodb.org/browse/PYTHON-785>`_.

.. versionchanged:: 2.8
   Deprecated.

.. versionadded:: 2.2
   The :class:`~pymongo.pool.Request` return value.
   :meth:`start_request` previously returned None
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
unset_lasterror_options


unset_lasterror_options
(self, *options)
DocString: DEPRECATED: Use :attr:`write_concern` instead.

Unset getlasterror options for this instance.

If no options are passed unsets all getlasterror options.
This does not set `safe` to False.

:Parameters:
    - `*options`: The list of options to unset.

.. versionchanged:: 2.4
   Deprecated unset_lasterror_options.
.. versionadded:: 2.0