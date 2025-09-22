البرمجة في FTC
==============

.. rst-class:: lead

البرمجة هي العقل الذي يتحكم في الروبوت. هنا نستعرض المنصات، أنماط التشغيل (OpModes)، المواضيع الأساسية، ونصائح للمبتدئين.

المنصات
-------

.. grid:: 1 3
   :gutter: 2

   .. card:: Java + Android Studio
      :icon: laptop-code
      :shadow: md

      :bdg-success:`الخيار الرسمي`  
      يدعم تطوير متكامل ومرن، ويوفر الوصول الكامل لمكتبات FTC SDK.

   .. card:: Blocks Programming
      :icon: cubes
      :shadow: md

      :bdg-info:`للمبتدئين`  
      برمجة مرئية بالسحب والإفلات. مثالية للفرق الجديدة.

   .. card:: Kotlin
      :icon: code
      :shadow: md

      مدعومة بشكل جزئي.  
      خيار حديث لمن لديهم خبرة سابقة.

OpModes
-------

.. tabs::

   .. tab:: Autonomous
      :bdg-warning:`مستقلة`

      الروبوت يعمل بالكود فقط (30 ثانية).  
      - التنقل التلقائي.  
      - استخدام الحساسات.  
      - تسجيل نقاط مبكرة.

   .. tab:: TeleOp
      :bdg-primary:`متحكم بها`

      السائقون يقودون الروبوت (120 ثانية).  
      - ربط الأزرار بالمحركات.  
      - التحكم في الآليات.  
      - سرعة استجابة عالية.

المواضيع الأساسية
-----------------

.. admonition:: ما يجب تعلمه
   :class: tip

   - **الحركة**: تشغيل المحركات والتحكم في السرعة.  
   - **PID Control**: للتحكم الدقيق بالمحركات.  
   - **الحساسات**:
     - IMU للاتجاه.
     - الكاميرا (EasyOpenCV) للرؤية الآلية.
   - **التنظيم**: استخدام Packages لتنظيم الكود.

نصائح للمبتدئين
---------------

.. grid:: 1 2
   :gutter: 2

   .. card:: الخطوة الأولى
      :icon: play
      :shadow: sm

      ابدأ بكتابة **TeleOp بسيط**:  
      ربط الأزرار بالمحركات فقط.

   .. card:: التطور التدريجي
      :icon: plus-circle
      :shadow: sm

      - أضف Autonomous تدريجيًا.  
      - جرب الحساسات خطوة بخطوة.  
      - اختبر الكود مبكرًا على الروبوت.

.. admonition:: تذكير مهم
   :class: important

   الكود الأفضل هو :bdg-success:`الأبسط والأكثر استقرارًا`.  
   لا تبدأ بحلول معقدة قبل إتقان الأساسيات.

الموارد
-------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - المصدر
     - الرابط
   * - GitHub الرسمي
     - https://github.com/FIRST-Tech-Challenge
   * - gm0 Programming Guide
     - https://gm0.org/en/latest/docs/software/index.html
   * - YouTube
     - قنوات مثل **FTC Tutorials**, **REV Robotics**
