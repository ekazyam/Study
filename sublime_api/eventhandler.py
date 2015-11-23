   def on_new(self, view):
        print('on_new')

    def on_new_async(self, view):
        print('on_new_async')

    def on_clone(self, view):
        print('on_clone')

    def on_clone_async(self, view):
        print('on_clone_async')

    def on_load(self, view):
        print('on_load')

    def on_load_async(self, view):
        print('on_load_async')

    def on_pre_close(self, view):
        print('on_pre_close')

    def on_close(self, view):
        print('on_close')

    def on_pre_save(self, view):
        print('on_pre_save')

    def on_pre_save_async(self, view):
        print('on_pre_save_asysnc')

    def on_post_save(self, view):
        print('on_post_save')

    def on_post_save_async(self, view):
        print('on_post_save_async')

    def on_modified(self, view):
        print('on_modified')

    def on_modified_async(self, view):
        print('on_modified_async')

    def on_selection_modified(self, view):
        print('on_selection_modified')

    def on_selection_modified_async(self, view):
        print('on_selection_modified_async')

    def on_activated(self, view):
        print('on_activated')

    def on_activated_async(self, view):
        print('on_activated_async')

    def on_deactivated(self, view):
        print('on_deactivated')

    def on_deactivated_async(self, view):
        print('on_deactivated_async')

    def on_text_command(self, view, command_name, args):
        print('on_text_command')

    def on_window_command(window, command_name, args):
        print('on_post_save_async')

    def post_text_command(self, view, command_name, args):
        print('post_text_command')

    def post_window_command(window, command_name, args):
        print('post_window_command')

    def on_query_context(self, view, key, operator, operand, match_all):
        print('on_query_context')
