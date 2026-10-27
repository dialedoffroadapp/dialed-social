# dialed-social

Images and week modules for Dialed Offroad's static social posts. Public so Instagram and Facebook can fetch the images by URL.

- `posts/<slug>/NN.jpg`: slides in posting order, 1080 x 1350 JPEG; `tNN.jpg` are the 540 x 675 thumbnails the Sunday Review page shows.
- `posts/manifest-<week>.json`: slug to image URL list for that week's queue.
- `tools/`: the renderer, the eight designs, fonts, the mark, and one module per week under `tools/weeks/`. `tools/README.md` is the contract for making a week.
- `out/<week>/`: the seed, SQL and review notes `publish_week.py` produced for that week.

Posting, comments and ads are handled by the `social-*` edge functions in the app's Supabase project; approvals happen on the Sunday Review page.
