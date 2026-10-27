# dialed-social

Images for Dialed Offroad social posts. Public so Instagram and Facebook can fetch them by URL.

- `posts/<slug>/NN.jpg`: slides in posting order, 1080x1350 JPEG.
- `posts/manifest-<week>.json`: slug to image URL list for that week's queue.

Nothing here is code. Posting is handled by the `social-publish` edge function in the app's Supabase project.
