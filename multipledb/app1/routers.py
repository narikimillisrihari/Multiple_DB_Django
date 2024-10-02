class CustomRouter:
    def db_for_read(self,model,**hints):
        if model._meta.app_label=='Student_details':
            return 'db1'
        elif model._meta.app_label=='Student_images':
            return 'db2'
        return None
    def db_for_write(self,model,**hints):
        if model._meta.app_label=='Student_details':
            return 'db1'
        elif model._meta.app_label=='Student_images':
            return 'db2'
        return None
    def allow_realtion(self,obj1,obj2,**hints):
        if obj1._meta.app_label == obj2._meta.app_label:
            return True
        return None
    def allow_migrate(self,db,app_label,model_name=None,**hints):
        if app_label=='Student_details':
            return db=='db1'
        elif app_label=='Student_images':
            return db=='db2'
        return None
