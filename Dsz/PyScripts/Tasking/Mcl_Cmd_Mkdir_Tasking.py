# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Mkdir_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.virtualdir
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.mkdir', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.mkdir.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['dir'] != None:
        dir = lpParams['dir']
    else:
        dir = ''
    try:
        dir = mcl.tasking.virtualdir.GetFullPath(dir)
    except:
        mcl.tasking.EchoError('Failed to apply virtual dir')
        return False

    tgtParams = mca.file.cmd.mkdir.Params()
    tgtParams.dir = dir
    rpc = mca.file.cmd.mkdir.tasking.RPC_INFO_CREATE
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.file.cmd.mkdir.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)