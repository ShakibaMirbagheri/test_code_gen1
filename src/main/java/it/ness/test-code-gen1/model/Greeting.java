package it.ness.test-code-gen1.model;

import it.ness.queryable.annotations.*;
import io.quarkus.hibernate.orm.panache.PanacheEntityBase;
import jakarta.persistence.*;
import static it.ness.test-code-gen1.management.AppConstants.GREETING_PATH;
import it.ness.test-code-gen1.model.enums.GreetingEnum;
import java.time.LocalDateTime;

@Entity
@Table(name = "greeetings")
@QRs(GREETING_PATH)
@QOrderBy("name asc")
public class Greeting extends PanacheEntityBase {

	@Id
	@Q
	@QList
	public String uuid;

	@QLike
	public String name;

	@Q
	public LocalDateTime date_time;

	@Q
	@Enumerated(EnumType.STRING)
	public GreetingEnum greetingEnum;

	@QLikeList
	public String tags;

	@QLogicalDelete
	boolean active;
}