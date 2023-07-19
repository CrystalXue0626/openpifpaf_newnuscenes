import openpifpaf

from .newnuscenes import newNuScenes


def register():
    openpifpaf.DATAMODULES['newnuscenes'] = newNuScenes
    openpifpaf.CHECKPOINT_URLS['shufflenetv2k16-nuscenes'] = 'http://github.com/DuncanZauss/' \
        'openpifpaf_assets/releases/download/v0.1.0/nuscenes_sk16.pkl.epoch150'
