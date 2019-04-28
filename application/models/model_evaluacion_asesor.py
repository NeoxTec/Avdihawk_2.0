import web
import app 

db = app.db

def get_all_evaluacion_asesor():
    try:
        return db.select('evaluacion_asesor')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None

def asesor_evaluado(asesoria):
    try:
        results = db.query('SELECT COUNT(*) as total FROM evaluacion_asesor WHERE asesoria=$asesoria', vars=locals())
        for dato in results:
            return dato.total
    except Exception as e:
        print "Model asesor_evaluado Error {}".format(e.args)
        print "Model asesor_evaluado Message {}".format(e.message)
        return None

def get_reporte_alumno(num_as):
    try:
        return db.select('evaluacion_asesor', where='asesoria = $num_as', vars=locals())[0]
    except Exception as e:
        print "Model get_reporte_asesor Error {}".format(e.args)
        print "Model get_reporte_asesor Message {}".format(e.message)
        return None

def get_evaluacion_asesor(id_e):
    try:
        return db.select('evaluacion_asesor', where='id_e=$id_e', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_evaluacion_asesor(id_e):
    try:
        return db.delete('evaluacion_asesor', where='id_e=$id_e', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_evaluacion_asesor(asesoria,horas,asistencia,comprension,razon,observaciones,calificacion,gusto):
    try:
        return db.insert('evaluacion_asesor',asesoria=asesoria,
horas=horas,
asistencia=asistencia,
comprension=comprension,
razon=razon,
observaciones=observaciones,
calificacion=calificacion,
gusto=gusto)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_evaluacion_asesor(id_e,asesoria,horas,asistencia,comprension,razon,observaciones,calificacion,gusto):
    try:
        return db.update('evaluacion_asesor',id_e=id_e,
asesoria=asesoria,
horas=horas,
asistencia=asistencia,
comprension=comprension,
razon=razon,
observaciones=observaciones,
calificacion=calificacion,
gusto=gusto,
                  where='id_e=$id_e',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
