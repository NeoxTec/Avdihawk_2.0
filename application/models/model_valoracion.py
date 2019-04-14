import web
import app

db = app.db


def get_all_valoracion():
    try:
        return db.select('valoracion')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_valoracion(asesoria):
    try:
        return db.select('valoracion', where='asesoria=$asesoria', vars=locals())
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_valoracion(num_val):
    try:
        return db.delete('valoracion', where='num_val=$num_val', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_valoracion(valor,asesoria):
    try:
        return db.insert('valoracion',valor=valor,
asesoria=asesoria)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_valoracion(num_val,valor,asesoria):
    try:
        return db.update('valoracion',num_val=num_val,
valor=valor,
asesoria=asesoria,
                  where='num_val=$num_val',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
