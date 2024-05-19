mport uuid
from datetime import datetime
import models



class BaseModel:
    
    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now
            self.updated_at = datetime.now
            models.storage.new(self)
    
    def save(self):
        self.updated_at = datetime.now
        models.storage.save()
    
    def __str__(self):
         return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def to_dict(self):
        n_dict = self.__dict__.copy()
        n_dict["__class__"] = self.__class__.__name__
        n_dict['created_at'] = self.__dict__['created_at'].isoformat()
        n_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        return (n_dict)

