w20e.pycms.news
===============

w20e.pycms news content type and listings. To use it in your PyCMS app,
add the egg dependency (usually in your buildout) and include the
package ZCML from your configure.zcml like so:

  <include package="w20e.pycms_news"/>

Now show the news listing viewlet in your template like:

  <div tal:content="structure view.render_viewlet('newslisting', limit=3)" />
