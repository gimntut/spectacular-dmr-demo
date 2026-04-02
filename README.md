# Demo project for connecting Django Modern Rest to an existing DRF project 
## Motivation
There are many projects in the world created using the Django Rest Framework (DRF). 
Many of them have already migrated to the latest versions of python and django. The only thing left is to switch to Django Modern Rest (dmr). 
But it's very difficult to do this, so you need to be able to make a smooth transition. 
In other words, you need to allow writing new APIs on dmr without rewriting the entire existing DRF API. 
This is prevented by the public interface - swagger/openapi. DRF has its own, and dmr has its own. 
No self-respecting company will make its users suffer by forcing them to use two swagger UI.

## Solution
You can create an adapter that allows you to connect dmr to an existing project with a stack of `django + drf + spectacular`.
As long as DRF is live in the project, the entire API will be available through its spectacular interface.
When the entire API is rewritten to dmr, it will be possible to switch to the new interface and throw out the `DRF + spectacular` bundle.

It seems that combining DRF and dmr in one project is not the most reasonable solution, because developers will have to work with two radically different approaches.
But this is offset by the fact that the risks associated with using the new technology are insured by having a reliable and proven backup option at hand.
At the same time, the potential benefits of using dmr are great.

The problem of a smooth transition from DRF exists in other frameworks as well: 
* [django-ninja](https://github.com/vitalik/django-ninja), 
* [django-bolt](https://github.com/dj-bolt/django-bolt), 
* [fastopenapi](https://fastopenapi.fatalyst.dev/frameworks/django/)

Perhaps no one needs a smooth transition. Or maybe no one thought about it, and whoever first suggests
it will get the maximum commercial advantage.

## Adapter distribution options
* A separate library. Pros: it doesn't clog up the dmr code. Cons: You need to promote it separately so that those who need
it can find out about it; someone needs to maintain this library.
* As part of the dmr. Advantages: The target audience shared with dmr, the fastest possible promotion and implementation. 
When DRF drops, it can be moved to a separate library. Cons: it is only indirectly related to dmr.
* As part of drf-spectacular. DRF-spectacular has a [special folder](https://github.com/tfranzel/drf-spectacular/tree/master/docs/blueprints ) for such things.
Pros: the most logical solution. Cons: no one will know that there is a new adapter; no one will be involved in support.

## About the project
This project is a proof-of-concept showing how to write a `dmr - spectacular` adapter.
The implementation is as naive as possible, based on the assumption that the swagger dmr interface is also published at some url.

Unfortunately, I don't have time for a full-fledged project with documentation and tests.

# Демо-проект подключения Django Modern Rest к существующему DRF-проекту 
## Мотивация
В мире существуют множество проектов созданных с использованием Django Rest Framework (DRF). 
Многие из них уже перешли на свежие версии python и django. Осталось дело за малым, перейти на Django Modern Rest (dmr). 
Но сделать это резко сложно, поэтому нужна возможность плавного перехода. 
Т.е. нужно позволить писать новые API на dmr, не переписывая весь существующий DRF-API. 
Этому препятствует публичный интерфейс - swagger/openapi. У DRF он свой, а у dmr - свой. 
Ни одна уважающая себя компания не заставит своих пользователей страдать, заставляя использовать два swagger ui.

## Решение
Можно создать адаптер, который позволяет подключить dmr в существующий проект со стеком `django + drf + spectacular`.
Пока в проекте будет жить DRF, весь API будет доступен через его интерфейс spectacular.
Когда весь API будет переписан на dmr, можно будет переключиться на новый интерфейс и выкинуть связку `DRF + spectacular`.

Кажется, что совмещение DRF и dmr в одном проекте это не самое разумное решение, т.к. разработчикам придётся работать с двумя кардинально различными подходами.
Но это компенсируется тем, риски связанные с использованием новой технологии, подстрахованы наличием под рукой надёжного и проверенного запасного варианта.
При этом потенциальный выигрыш от использования dmr велик.

Проблема плавного перехода с DRF есть и в других фреймворках: 
* [django-ninja](https://github.com/vitalik/django-ninja), 
* [django-bolt](https://github.com/dj-bolt/django-bolt), 
* [fastopenapi](https://fastopenapi.fatalyst.dev/frameworks/django/)

Возможно, плавный переход никому не нужен. А возможно, об этом никто не думал, и тот, кто первый такое предложит,
тот и получит максимальное коммерческое преимущество.

## Варианты распространения адаптера
* Отдельная библиотека. Плюсы: не засоряет код dmr. Минусы: Нужно отдельно её продвигать, чтобы те, кто в ней нуждаются, 
могли о ней узнать; кто-то должен поддерживать эту библиотеку
* В составе dmr. Плюсы: Общая с dmr целевая аудитория, максимально быстрое продвижение и внедрение. 
Когда DRF падёт, можно вынести в отдельную библиотеку. Минусы: имеет только косвенное отношение к dmr.
* В составе drf-spectacular. У drf-spectacular есть [специальная папка](https://github.com/tfranzel/drf-spectacular/tree/master/docs/blueprints) для таких вещей.
Плюсы: самое логичное решение. Минусы: никто не узнает, что там появился новый адаптер; никто не будет заниматься поддержкой.

## О проекте
Данный проект - proof-of-concept показывающий как можно написать адаптер `dmr - spectacular`.
Реализация максимально наивная, основанная на предположении, что интерфейс swagger dmr тоже опубликован по какому-либо url.

К сожалению, времени на полноценный проект, с документацией и тестами, у меня нет.

## Demonstration / Демонстрация

### Installation / Установка
```shell
git clone https://github.com/gimntut/spectacular-dmr-demo.git
cd spectacular-dmr-demo/
uv run src/manage.py migrate
```

### Launch / Запуск
```shell
uv run src/manage.py runserver
```

### Application / Работа приложения
* http://localhost:8000/api/schema/swagger-ui/ - объединённый swagger
* http://localhost:8000/api/dmr/docs/swagger/ - dmr-swagger

### Notes to the code / Примечания к коду
* `src/adapter/hooks.py` - файл с кодом адаптера
* `src/config/settings/s20_applicaton.py` - файл настроек, в котором происходит подключение 

#### Adapter connection code / Код подключения адаптера
```python
SPECTACULAR_SETTINGS = {
    ...
    # !!! Вот здесь происходит подключение адаптера !!!
    "POSTPROCESSING_HOOKS": ["adapter.hooks.dmr_adapter_hook"],
}
```
