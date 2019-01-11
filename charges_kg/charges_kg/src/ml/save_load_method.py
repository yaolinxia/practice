import os
import pickle
import logging
logging.getLogger().setLevel(logging.INFO)
# 存储模型
def save_model(mpath, mname, obj):
    try:
        with open(os.path.join(mpath, mname), 'wb') as f:
            pickle.dump(obj, f)
        logging.info("Successfully saved models %s to %s" % (mname, os.path.join(mpath, mname)))
    except:
        if not os.path.exists(mpath):
            os.makedirs(mpath)
        logging.info('Successfully made directory %s' % mpath)
        with open(os.path.join(mpath, mname), 'wb') as f:
            pickle.dump(obj, f)
        logging.info("Successfully saved %s from %s" % (mname, os.path.join(mpath, mname)))

# 读取模型
def load_model(mpath, mname):
    with open(os.path.join(mpath, mname), 'rb') as f:
        obj = pickle.load(f)
    logging.info("Successfully loaded %s from %s" % (mname, mpath))
    return obj