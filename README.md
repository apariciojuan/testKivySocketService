# testKivySocketService
Prueba servicio desde android
Solo es para probar conexion desde android usando Kivy y python, mediante un servicio persistente a un server. 
Tambien se inicia automaticante en caso de un reinicio.

Python 2.7.2

kivy 1.9.1

La carpeta server contiene el servidor de prueba para recibir los datos e ir solicitando mas al cliente que responde con recibido confirmando la conexion desde android.

SI queremos que se auto ejecute cuando reiniciamos el equipos debemos agregar todo esto:

El archivo MyBroadcastReceiver.java debe colorcarse android/python-for-android/dist/default/src, lo mas seguro es que cambie acorde al proyecto, pero si no esta asi la ruta colocarlo donde este el archivo PythonActivity.java.

Ahora solo falta modificar el AndroidManifest.tmpl.xml que es el templeate para cuando crea el AndroidManifest, a este le agregamos dentro y justo al principio de la etiqueta <application> lo siguiente:
  
  <receiver android:name=".MyBroadcastReceiver" android:enabled="true" >
    <intent-filter><action android:name="android.intent.action.BOOT_COMPLETED" /></intent-filter>
</receiver>

Esto lo tienen detallado en ingles en la fuente:
https://github.com/kivy/kivy/wiki/Starting-Kivy-service-on-bootup-(Android)
