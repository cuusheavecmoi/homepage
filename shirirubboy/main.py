#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class BaseHandler(webapp2.RequestHandler):
  def render_template(self, filename, **template_args):
      template_values = {}
      template = JINJA_ENVIRONMENT.get_template('/static/' + filename)
      self.response.write(template.render(template_values))


class IndexHandler(BaseHandler):
  def get(self):
    self.render_template('home.html', name=self.request.get('name'))


app = webapp2.WSGIApplication([
    ('/', IndexHandler)
], debug=True)
